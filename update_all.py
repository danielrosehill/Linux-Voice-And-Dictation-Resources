#!/usr/bin/env python3
"""
Complete repository update script for Linux-STT-And-Voice-Assistants.

This script:
1. Extracts GitHub repos from README.md
2. Fetches current star counts and metadata from GitHub API
3. Updates data/repos.json
4. Regenerates projects-by-stars.md
5. Updates the "Last Updated" badge in README.md
6. Commits and pushes changes to GitHub

Usage:
    python update_all.py           # Full update with API fetch and push
    python update_all.py --no-push # Update locally without pushing
    python update_all.py --no-fetch # Use cached data, regenerate markdown only
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


def run_command(cmd: List[str], cwd: Path = None) -> tuple[bool, str]:
    """Run a shell command and return success status and output."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
            cwd=cwd
        )
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)


def extract_github_repos_from_readme(readme_path: Path) -> List[Dict[str, str]]:
    """Extract all GitHub repository URLs from README.md."""
    repos = []
    content = readme_path.read_text(encoding='utf-8')

    # Pattern to match GitHub repository links in markdown format
    github_pattern = r'\[([^\]]*)\]\(https://github\.com/([^/]+)/([^/)]+)\)'
    matches = re.findall(github_pattern, content)

    for match in matches:
        display_name, owner, repo = match
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
                'forks': data.get('forks_count', 0),
                'open_issues': data.get('open_issues_count', 0),
            }
        else:
            print(f"    Warning: Failed to fetch {owner}/{repo}")
            return None
    except Exception as e:
        print(f"    Warning: Error fetching {owner}/{repo}: {e}")
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
    delay: float = 0.25
) -> Dict:
    """Update repository data, optionally fetching from API."""
    repos_dict = existing_data.get('repos', {})
    current_repo_keys = set()

    for i, repo_info in enumerate(readme_repos):
        key = f"{repo_info['owner']}/{repo_info['repo']}"
        current_repo_keys.add(key)

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
            repos_dict[key]['name'] = repo_info['name']
            repos_dict[key]['url'] = repo_info['url']

        if fetch_api:
            print(f"  [{i+1}/{len(readme_repos)}] {key}")
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

    for key in repos_dict:
        repos_dict[key]['in_readme'] = key in current_repo_keys

    return {
        'repos': repos_dict,
        'metadata': {
            'last_updated': datetime.now(timezone.utc).isoformat(),
            'total_repos': len([k for k in repos_dict if repos_dict[k].get('in_readme', True)]),
        }
    }


def generate_projects_by_stars(data: Dict, output_path: Path) -> None:
    """Generate projects-by-stars.md from JSON data."""
    repos = data.get('repos', {})
    metadata = data.get('metadata', {})

    active_repos = [
        {**info, 'key': key}
        for key, info in repos.items()
        if info.get('in_readme', True)
    ]
    active_repos.sort(key=lambda x: x.get('stars', 0), reverse=True)

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

        if len(description) > 100:
            description = description[:97] + '...'
        description = description.replace('|', '\\|')

        archived_marker = ' (archived)' if repo.get('archived', False) else ''

        content += f"| {i} | [**{name}**]({url}){archived_marker} | {stars:,} | {language} | {description} |\n"

    content += """
---

*Data source: GitHub API via `gh` CLI*
"""

    output_path.write_text(content, encoding='utf-8')


def update_readme_date(readme_path: Path) -> None:
    """Update the Last Updated badge in README.md."""
    content = readme_path.read_text(encoding='utf-8')

    today = datetime.now().strftime('%B %d, %Y').replace(' 0', ' ')
    today_encoded = today.replace(' ', '%20').replace(',', '%2C')

    # Update the Last Updated badge
    pattern = r'!\[Last Updated\]\(https://img\.shields\.io/badge/Last%20Updated-[^)]+\)'
    replacement = f'![Last Updated](https://img.shields.io/badge/Last%20Updated-{today_encoded}-blue?style=flat-square)'

    new_content = re.sub(pattern, replacement, content)

    # Update resource count badge if present
    readme_path.write_text(new_content, encoding='utf-8')


def git_commit_and_push(root: Path, push: bool = True) -> bool:
    """Commit changes and optionally push to remote."""
    print("\n4. Committing changes...")

    # Add all changed files
    success, _ = run_command(['git', 'add', '-A'], cwd=root)
    if not success:
        print("   Failed to stage files")
        return False

    # Check if there are changes to commit
    success, output = run_command(['git', 'status', '--porcelain'], cwd=root)
    if not output.strip():
        print("   No changes to commit")
        return True

    # Commit
    today = datetime.now().strftime('%Y-%m-%d')
    commit_msg = f"Update star counts and project data ({today})"

    success, output = run_command(['git', 'commit', '-m', commit_msg], cwd=root)
    if not success:
        print(f"   Failed to commit: {output}")
        return False
    print(f"   Committed: {commit_msg}")

    if push:
        print("\n5. Pushing to remote...")
        success, output = run_command(['git', 'push'], cwd=root)
        if not success:
            print(f"   Failed to push: {output}")
            return False
        print("   Pushed successfully")

    return True


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Update repository data, regenerate markdown, and push to GitHub'
    )
    parser.add_argument(
        '--no-push',
        action='store_true',
        help='Skip pushing to remote (local update only)'
    )
    parser.add_argument(
        '--no-fetch',
        action='store_true',
        help='Skip fetching from GitHub API (use cached data)'
    )
    parser.add_argument(
        '--delay',
        type=float,
        default=0.25,
        help='Delay between API calls in seconds (default: 0.25)'
    )

    args = parser.parse_args()

    root = get_project_root()
    readme_path = root / 'README.md'
    data_dir = root / 'data'
    json_path = data_dir / 'repos.json'
    stars_path = root / 'projects-by-stars.md'

    data_dir.mkdir(exist_ok=True)

    print("=" * 60)
    print("Linux STT Repository Updater")
    print("=" * 60)

    # Step 1: Extract repos from README
    print("\n1. Extracting repositories from README.md...")
    readme_repos = extract_github_repos_from_readme(readme_path)

    # Deduplicate
    seen = set()
    unique_repos = []
    for repo in readme_repos:
        key = f"{repo['owner']}/{repo['repo']}"
        if key not in seen:
            seen.add(key)
            unique_repos.append(repo)

    print(f"   Found {len(unique_repos)} unique repositories")

    # Step 2: Fetch and update data
    print("\n2. Updating repository data...")
    existing_data = load_existing_data(json_path)

    if args.no_fetch:
        print("   Skipping API fetch (using cached data)")
        data = existing_data
        # Still update in_readme flags
        current_keys = {f"{r['owner']}/{r['repo']}" for r in unique_repos}
        for key in data.get('repos', {}):
            data['repos'][key]['in_readme'] = key in current_keys
    else:
        data = update_repo_data(
            existing_data,
            unique_repos,
            fetch_api=True,
            delay=args.delay
        )

    # Save JSON
    json_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )
    print(f"   Saved {json_path}")

    # Step 3: Generate markdown and update README
    print("\n3. Generating projects-by-stars.md...")
    generate_projects_by_stars(data, stars_path)
    print(f"   Generated {stars_path}")

    print("   Updating README.md date badge...")
    update_readme_date(readme_path)

    # Step 4 & 5: Commit and push
    git_commit_and_push(root, push=not args.no_push)

    # Summary
    repos = data.get('repos', {})
    active = [r for r in repos.values() if r.get('in_readme', True)]

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  Total repos: {len(active)}")
    print(f"  1000+ stars: {len([r for r in active if r.get('stars', 0) >= 1000])}")
    print(f"  100+ stars:  {len([r for r in active if r.get('stars', 0) >= 100])}")

    top_5 = sorted(active, key=lambda x: x.get('stars', 0), reverse=True)[:5]
    print("\n  Top 5:")
    for r in top_5:
        print(f"    {r.get('stars', 0):>6,} - {r['owner']}/{r['repo']}")

    print("\nDone!")


if __name__ == "__main__":
    main()
