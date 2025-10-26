#!/bin/bash

# sudo wget https://github.com/ddo/fast/releases/download/v0.0.4/fast_linux_amd64 -O /usr/bin/fast

# sudo chmod +x /usr/bin/fast

yay -Sy --noconfirm fast-bin

sudo modprobe nct6775

echo nct6775 | sudo tee /etc/modules-load.d/nct6775.conf

sudo sensors-detect --auto

# ssh-keygen -t rsa
# cat ~/.ssh/id_rsa.pub | ssh -p 3389 renata@192.168.15.3 'cat >> .ssh/authorized_keys'

sudo crontab -l -u renata | cat - ../assets/crontab.txt | sudo crontab -u renata - && crontab -l

sh ../assets/Conky/install-conky.sh

if [ ! -d ~/.config/autostart ]; then
	mkdir ~/.config/autostart
fi

cp -v ../assets/autostart/* ~/.config/autostart

if [ ! -d ~/Documents/LinuxCustomizations/MinimalisConky ]; then
	cp -v ~/Documents/LinuxCustomizations/MinimalisConky/conky-sed.conf ~/.config/conky/
fi


