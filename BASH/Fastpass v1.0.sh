#!/bin/bash

# budlabs mini install: makes a profile, installs the tools you need and pulls the latest recon Scripts from repo that your working on.

# pulls to latest mobile setup and bc profile.
sudo apt update 

sudo apt upgrade -y 

sudo apt autoremove -y 

usermod -aG sudo budlabs 

# Code for tooling and dependencies

# coin ticker with snap store 
sudo apt install snapd -y 
sudo snap install cointop --stable

# Pentesting Tools
sudo apt-get install nmap -y
sudo apt-get install -y aircrack-ng

# python libraries 
pip install cinemagoer
pip install tk
pip install matplotlib
pip install ez_setup
pip install moviepy
pip install pytube

# docker install and profile setup for lab containers
curl -fsSL https://get.docker.com -o get-docker.sh

sudo bash get-docker.sh

sudo usermod -aG docker budlabs

# Latest Working Tools 
git clone https://github.com/BCBUUD/Tools.git

# install youtube and download playlist...
curl https://yt-dl.org/latest/youtube-dl -o /usr/local/bin/youtube-dl

chmod a+rx /usr/local/bin/youtube-dl

sleep 5
mkdir documents
mkdir downloads
mkdir Desk
mkdir Help 
mkdir Music

sleep 5

cd Music

# download playlist with latest addons of music added 
youtube-dl --ignore-errors --format bestaudio --extract-audio --audio-format mp3 
--audio-quality 160K --output "%(title)s.%(ext)s" --yes-playlist https://youtube.com/playlist?list=PLCG7tuydajnzUT6-6CXjmaMh5IEm_9-zn

cd

echo "Profile Installed. Tools are Ready in /Tools..."

echo "sudo snap run cointop to see coin tickers"

sleep 10 

clear



if [ ! -e DockerCheatSheet.txt]; 
then 
        echo "How to use Docker:

        Pull images:

        make new containers:

        Delete Containers:

        Name Containers:" >> DockerCheatSheet.txt | cat DockerCheatSheet.txt 
else
        echo "Already Exist."
fi 