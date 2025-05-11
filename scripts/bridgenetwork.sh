#!/bin/fish

if test (count $argv) = 1
    set BR_INT $argv[1]
    set BR_NAME br10
    set SUBNET_IP 172.31.1.100/24
    set CON_ID (nmcli con show | grep $BR_INT | awk '{print $4}')
       
    sudo nmcli con delete $CON_ID
    sudo nmcli connection add type bridge autoconnect yes con-name $BR_NAME ifname $BR_NAME
    sudo nmcli connection modify $BR_NAME ipv4.addresses $SUBNET_IP ipv4.method manual
    sudo nmcli connection add type bridge-slave autoconnect yes con-name $BR_INT ifname $BR_INT master $BR_NAME
    
    sudo virsh  net-define ~/SystemInfo/config-bridge.xml
    sudo virsh net-list --all
    sudo virsh  net-start --network BridgeNet01
    sudo virsh net-autostart BridgeNet01
else
    printf "Use mode: ./0D_Bridge_Network.sh if_name\n"
    printf "Example: ./0D_Bridge_Network.sh enp7s0\n"
end
