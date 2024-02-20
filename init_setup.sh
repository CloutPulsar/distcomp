#!/bin/bash

# Update system packages
echo "Updating system packages..."
sudo apt-get update && sudo apt-get upgrade -y

# Install Docker
echo "Installing Docker..."
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add current user to the Docker group
echo "Adding the current user to the Docker group..."
sudo usermod -aG docker $USER

# Install FFmpeg for video processing
echo "Installing FFmpeg..."
sudo apt-get install -y ffmpeg

# Clean up
echo "Cleaning up..."
rm get-docker.sh

echo "Setup complete. Please reboot your device to apply all changes."
