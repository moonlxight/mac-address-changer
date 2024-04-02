import os
import sys
import requests
import random
import colorama
import subprocess
import arts
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

try:
    stderr.writelines(Fore.LIGHTYELLOW_EX+arts.dev)
    clear()
    stderr.writelines(Fore.RED+arts.mac_address+Fore.LIGHTCYAN_EX+arts.changer)
except Exception as e:
    stderr.writelines("An error has occured!")

def display_menu():
    print("\033[1;93m[01] Start\033[0m")

display_menu()
input()