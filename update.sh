#!/bin/bash
# Update script for Linux-STT-And-Voice-Assistants
# Activates venv and runs the update script

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

source .venv/bin/activate
python update_all.py "$@"
