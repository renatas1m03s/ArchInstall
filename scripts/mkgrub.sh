#!/bin/bash

sed -i 's/loglevel=3 quiet/quiet loglevel=3 splash split_lock_detect=off/g' /etc/default/grub

grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=arch_grub --recheck
grub-mkconfig -o /boot/grub/grub.cfg
