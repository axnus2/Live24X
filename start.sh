#!/bin/bash
# Make sure FFmpeg is installed on Render instance
apt-get update && apt-get install -y ffmpeg
# Start the bot
python3 bot.py
