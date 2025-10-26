#!/bin/bash

sed -i 's/base udev autodetect microcode modconf kms keyboard keymap consolefont/systemd autodetect microcode modconf kms keyboard sd-vconsole plymouth/g' /etc/mkinitcpio.conf
