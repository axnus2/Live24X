#!/bin/bash
# Render start script for Telegram bot + FFmpeg streaming

# Update system packages
apt-get update -y

# Install ffmpeg
apt-get install -y ffmpeg

# Upgrade pip
python -m pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Start Telegram bot
python bot.py
