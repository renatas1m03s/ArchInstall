#!/bin/bash

## Bash script - basic archlinux install
## By Renata Maria - renata.s1m03s@gmail.com
## 
## This install basic components to achive a minimal functional Arch Linux System
##
## Version 0.1
##

echo -e "\n\n########################################################\n\n    Preparing system for ArchLinux\n\n########################################################\n\n"

echo -e "\n############ Mounting RAM Drive ############\n"

mkdir /root/ArchInstall
mount -t tmpfs -o size=1024m ArchSetup /root/ArchInstall
sleep 2

echo -e "\n############ Installing dependencies ############\n"

pacman -Sy --noconfirm archlinux-keyring
pacman-key --init
pacman-key --populate archlinux
pacman -Sy --noconfirm --needed git python-blessed p7zip parted dosfstools

echo -e "\n############ Downloading setup wizard files ############\n"

git clone https://github.com/renatas1m03s/ArchInstall /root/ArchInstall

echo -e "\n\n#### All ready to start ####"
echo -e "\n"
echo -e "- For default options, run './ArchInstall/install'"
echo -e "- With parameters (self-explained), run './ArchInstall/install -s hostname -u username -c \"display user name\" -p password'"
echo -e "  Ex.: ./ArchInstall/install -s archserver -u jane -c \"jane Doe\" -p P@ssw0rd'"
echo -e "- To print help, run './ArchInstall/install -h'"
echo -e "\n"
