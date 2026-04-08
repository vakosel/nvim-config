#!/bin/bash
TARGET="$1"

# If it's a file, switch to its directory
[ -f "$TARGET" ] && TARGET="$(dirname "$TARGET")"

wezterm start --cwd="$TARGET"
