#!/bin/bash

echo $1 | passwd --stdin

echo $1 | passwd $2 --stdin

echo $2' ALL=(ALL) ALL' | sudo EDITOR='tee -a' visudo
echo $2' ALL=(ALL) NOPASSWD: /usr/bin/pacman' | sudo EDITOR='tee -a' visudo
