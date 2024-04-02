import os
import sys
import requests
import random
import colorama
import art
import re
from os import system, name
from sys import stdout, stderr
from colorama import Fore, Style, init
init()

charList = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
newMac = ""
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
clear()
system("title TwistyJead's Mac Address Changer Tool")
stderr.writelines(art.mac_address_changer)
input()