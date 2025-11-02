#!/bin/bash

sed -i 's/loglevel=3 quiet/quiet loglevel=3 splash split_lock_detect=off/g' /etc/default/grub
sed -i 's/#GRUB_DISABLE_OS_PROBER/GRUB_DISABLE_OS_PROBER/g' /etc/default/grub

grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=arch_grub --recheck
cd /home/$1/ArchInstall/assets/GrubTheme
./install.sh
