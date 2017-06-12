#!/usr/bin/env python
# coding=utf-8
# code By:
###############################################
##   __                     _               ###
##  / _|                   (_)           ######
## | |_ ___ _ __   __ _ _____          ########
## |  _/ _ \ '_ \ / _` |_  / |               #
## | ||  __/ | | | (_| |/ /| |               ##               
## |_| \___|_| |_|\__, /___|_|               ######
##                 __/ |                     #######
##                |___/                      ########
##################################################

import os

os.system('apt-get update && apt-get dist-upgrade -y')
os.system('apt-get install python-dev -y')
os.system('apt-get install gcc -y')
os.system('apt-get install rfkill -y')
os.system('apt-get -y install isc-dhcp-server')
os.system('wget wget https://bootstrap.pypa.io/get-pip.py')
os.system('python get-pip.py')
os.system('pip install -U web.py')
os.system('pip install -U psutil')
os.system('pip install -U scapy')
