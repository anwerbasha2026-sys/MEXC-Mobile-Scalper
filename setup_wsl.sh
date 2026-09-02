#!/bin/bash
set -e

echo "=== MEXC Mobile Scalper - WSL2 Android Build Setup ==="
echo

sudo apt update
sudo apt install -y \
  git zip unzip openjdk-17-jdk python3-pip python3-venv \
  autoconf libtool pkg-config zlib1g-dev libncurses5-dev \
  libncursesw5-dev cmake libffi-dev libssl-dev

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip setuptools wheel
python -m pip install "cython<3.0" buildozer

echo
echo "Setup complete."
echo "Now run:"
echo "  source .venv/bin/activate"
echo "  buildozer android debug"
echo
echo "The APK will be created in the bin/ folder."
