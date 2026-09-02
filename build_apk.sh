#!/bin/bash
set -e

if [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
fi

echo "=== Building APK ==="
buildozer android debug

echo
echo "=== Build finished ==="
echo "APK files:"
ls -lh bin/*.apk 2>/dev/null || true
