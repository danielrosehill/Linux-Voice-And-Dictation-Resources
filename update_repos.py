#!/usr/bin/env python3
"""
Repository metadata updater for Linux-STT-And-Voice-Assistants.

This script:
1. Extracts GitHub repos from README.md
2. Fetches current metadata from GitHub API
3. Updates the JSON data file
4. Generates the projects-by-stars.md page

Can be run as a pre-commit hook or manually.
"""

import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional


def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent


def extract_github_repos_from_readme(readme_path: Path) -> List[Dict[str, str]]:
    """Extract all GitHub repository URLs from README.md."""
    repos = []

    content = readme_path.read_text(encoding='utf-8')

    # Pattern to match GitHub repository links in markdown format
    # Matches: [text](https://github.com/owner/repo)
    github_pattern = r'\[([^\]]*)\]\(https://github\.com/([^/]+)/([^/)]+)\)'
    matches = re.findall(github_pattern, content)

    for match in matches:
        display_name, owner, repo = match
        # Clean up repo name (remove any trailing characters)
        repo = repo.split('?')[0].split('#')[0].rstrip('/')

        # Skip topics and other non-repo GitHub URLs
        if owner == 'topics':
            continue

        repos.append({
            'name': display_name.replace('**', '').strip(),
            'owner': owner,
            'repo': repo,
            'url': f"https://github.com/{owner}/{repo}"
        })

    return repos


def get_repo_info_from_api(owner: str, repo: str) -> Optional[Dict]:
    """Fetch repository information using GitHub CLI."""
    try:
        cmd = ['gh', 'api', f'/repos/{owner}/{repo}']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

        if result.returncode == 0:
            data = json.loads(result.stdout)
            return {
                'stars': data.get('stargazers_count', 0),
                'description': data.get('description', ''),
                'last_updated': data.get('updated_at', ''),
                'language': data.get('language', ''),
                'archived': data.get('archived', False),
                'topics': data.get('topics', []),
                'default_branch': data.get('default_branch', 'main'),
                'forks': data.get('forks_count', 0),
                'open_issues': data.get('open_issues_count', 0),
            }
        else:
            print(f"  Warning: Failed to fetch {owner}/{repo}: {result.stderr.strip()}")
            return None
    except subprocess.TimeoutExpired:
        print(f"  Warning: Timeout fetching {owner}/{repo}")
        return None
    except Exception as e:
        print(f"  Warning: Error fetching {owner}/{repo}: {e}")
        return None


def load_existing_data(json_path: Path) -> Dict:
    """Load existing JSON data if it exists."""
    if json_path.exists():
        return json.loads(json_path.read_text(encoding='utf-8'))
    return {'repos': {}, 'metadata': {}}


def update_repo_data(
    existing_data: Dict,
    readme_repos: List[Dict],
    fetch_api: bool = True,
    delay: float = 0.3
) -> Dict:
    """Update repository data, optionally fetching from API."""
    repos_dict = existing_data.get('repos', {})

    # Track which repos are still in README
    current_repo_keys = set()

    for i, repo_info in enumerate(readme_repos):
        key = f"{repo_info['owner']}/{repo_info['repo']}"
        current_repo_keys.add(key)

        # Initialize or update basic info
        if key not in repos_dict:
            repos_dict[key] = {
                'name': repo_info['name'],
                'owner': repo_info['owner'],
                'repo': repo_info['repo'],
                'url': repo_info['url'],
                'stars': 0,
                'description': '',
                'language': '',
                'archived': False,
                'last_api_update': None,
            }
        else:
            # Update name if it changed in README
            repos_dict[key]['name'] = repo_info['name']
            repos_dict[key]['url'] = repo_info['url']

        # Fetch from API if requested
        if fetch_api:
            print(f"  [{i+1}/{len(readme_repos)}] Fetching {key}...")
            api_data = get_repo_info_from_api(repo_info['owner'], repo_info['repo'])

            if api_data:
                repos_dict[key].update({
                    'stars': api_data['stars'],
                    'description': api_data['description'] or '',
                    'language': api_data['language'] or '',
                    'archived': api_data['archived'],
                    'last_updated': api_data['last_updated'],
                    'topics': api_data['topics'],
                    'forks': api_data['forks'],
                    'open_issues': api_data['open_issues'],
                    'last_api_update': datetime.now(timezone.utc).isoformat(),
                })

            time.sleep(delay)

    # Mark repos no longer in README (but don't delete them)
    for key in repos_dict:
        repos_dict[key]['in_readme'] = key in current_repo_keys

    return {
        'repos': repos_dict,
        'metadata': {
            'last_updated': datetime.now(timezone.utc).isoformat(),
            'total_repos': len([k for k in repos_dict if repos_dict[k].get('in_readme', True)]),
            'readme_extraction_date': datetime.now(timezone.utc).isoformat(),
        }
    }


def generate_projects_by_stars(data: Dict, output_path: Path) -> None:
    """Generate projects-by-stars.md from JSON data."""
    repos = data.get('repos', {})
    metadata = data.get('metadata', {})

    # Filter to repos still in README and sort by stars
    active_repos = [
        {**info, 'key': key}
        for key, info in repos.items()
        if info.get('in_readme', True)
    ]
    active_repos.sort(key=lambda x: x.get('stars', 0), reverse=True)

    # Format the update timestamp
    last_updated = metadata.get('last_updated', '')
    if last_updated:
        try:
            dt = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
            date_str = dt.strftime('%B %d, %Y at %H:%M UTC')
        except Exception:
            date_str = last_updated
    else:
        date_str = 'Unknown'

    content = f"""# Projects by Stars

All repositories from the Linux STT and Voice Assistants index, sorted by GitHub star count from highest to lowest.

**Last updated:** {date_str}

*This page is auto-generated from [repos.json](data/repos.json). Star counts are fetched from the GitHub API.*

---

## Summary

- **Total Projects:** {len(active_repos)}
- **Projects with 1000+ stars:** {len([r for r in active_repos if r.get('stars', 0) >= 1000])}
- **Projects with 100+ stars:** {len([r for r in active_repos if r.get('stars', 0) >= 100])}

---

## All Projects

| Rank | Repository | Stars | Language | Description |
|------|------------|-------|----------|-------------|
"""

    for i, repo in enumerate(active_repos, 1):
        name = repo.get('name', repo.get('repo', 'Unknown'))
        url = repo.get('url', '')
        stars = repo.get('stars', 0)
        language = repo.get('language', 'N/A') or 'N/A'
        description = repo.get('description', '') or 'No description'

        # Truncate long descriptions
        if len(description) > 100:
            description = description[:97] + '...'

        # Escape pipe characters in description
        description = description.replace('|', '\\|')

        archived_marker = ' ⚠️' if repo.get('archived', False) else ''

        content += f"| {i} | [**{name}**]({url}){archived_marker} | {stars:,} | {language} | {description} |\n"

    # Add legend
    content += """
---

*⚠️ = Archived repository*

*Data source: GitHub API via `gh` CLI*
"""

    output_path.write_text(content, encoding='utf-8')
    print(f"Generated {output_path}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Update repository metadata and generate projects-by-stars.md'
    )
    parser.add_argument(
        '--no-fetch',
        action='store_true',
        help='Skip fetching from GitHub API (use cached data only)'
    )
    parser.add_argument(
        '--json-only',
        action='store_true',
        help='Only update JSON, do not generate markdown'
    )
    parser.add_argument(
        '--markdown-only',
        action='store_true',
        help='Only generate markdown from existing JSON'
    )
    parser.add_argument(
        '--delay',
        type=float,
        default=0.3,
        help='Delay between API calls in seconds (default: 0.3)'
    )

    args = parser.parse_args()

    root = get_project_root()
    readme_path = root / 'README.md'
    data_dir = root / 'data'
    json_path = data_dir / 'repos.json'
    output_path = root / 'projects-by-stars.md'

    # Ensure data directory exists
    data_dir.mkdir(exist_ok=True)

    if args.markdown_only:
        # Just regenerate markdown from existing JSON
        if not json_path.exists():
            print(f"Error: {json_path} does not exist. Run without --markdown-only first.")
            sys.exit(1)

        data = load_existing_data(json_path)
        generate_projects_by_stars(data, output_path)
        return

    print("Extracting repositories from README.md...")
    readme_repos = extract_github_repos_from_readme(readme_path)

    # Deduplicate by owner/repo
    seen = set()
    unique_repos = []
    for repo in readme_repos:
        key = f"{repo['owner']}/{repo['repo']}"
        if key not in seen:
            seen.add(key)
            unique_repos.append(repo)

    print(f"Found {len(unique_repos)} unique repositories")

    # Load existing data
    existing_data = load_existing_data(json_path)

    # Update data
    if not args.no_fetch:
        print("\nFetching repository data from GitHub API...")

    data = update_repo_data(
        existing_data,
        unique_repos,
        fetch_api=not args.no_fetch,
        delay=args.delay
    )

    # Save JSON
    json_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )
    print(f"\nSaved {json_path}")

    # Generate markdown
    if not args.json_only:
        generate_projects_by_stars(data, output_path)

    # Print summary
    repos = data.get('repos', {})
    active = [r for r in repos.values() if r.get('in_readme', True)]
    print(f"\nSummary:")
    print(f"  Total repos in README: {len(active)}")
    print(f"  Repos with 1000+ stars: {len([r for r in active if r.get('stars', 0) >= 1000])}")
    print(f"  Repos with 100+ stars: {len([r for r in active if r.get('stars', 0) >= 100])}")

    top_5 = sorted(active, key=lambda x: x.get('stars', 0), reverse=True)[:5]
    print(f"\nTop 5 by stars:")
    for r in top_5:
        print(f"  {r.get('stars', 0):,} - {r['owner']}/{r['repo']}")


if __name__ == "__main__":
    main()
