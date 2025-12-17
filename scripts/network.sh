#!/bin/fish

# Parameters for onboard connection
set ADAPTER1 (ip link show | grep -B 1 "60:dd:ea:51" | grep enp16 | awk -F':' '{print $2}')
set CONECTION1 (nmcli con show | grep $ADAPTER1 | awk '{print $1" "$2" "$3}')
set CONECTION1_NEWNAME "Onboard"

# Configuring onboard connection to a fixed ip adddress

nmcli con mod $CONECTION1 connection.id $CONECTION1_NEWNAME
nmcli con mod $CONECTION1_NEWNAME ipv4.addresses 192.168.1.10/24
nmcli con mod $CONECTION1_NEWNAME ipv4.gateway 192.168.1.254
nmcli con mod $CONECTION1_NEWNAME ipv4.dns "192.168.1.1 192.168.15.2"
nmcli con mod $CONECTION1_NEWNAME ipv4.method manual
nmcli con down $CONECTION1_NEWNAME && nmcli con up $CONECTION1_NEWNAME

sed -i 's/#Port 22/Port 3389/g' /etc/ssh/sshd_config
