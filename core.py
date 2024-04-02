import os
import sys
import random
import subprocess
import arts
import re
import configparser
from os import system, name
from sys import stdout, stderr
from colorama import Fore, Style, init

init()
def read_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config['Network']['interface_name']
def mac_changer():
    charList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    newMac = ""
    for i in range(6):
        newMac += random.choice(charList) + random.choice(charList)
        if i < 5:
            newMac += ":"
    try:
        # Check the network interface name (You can customize this based on your system)
        #interface_name = "eth0"
        interface_name = read_config()
        # Check the current MAC address
        ifconfigResult = subprocess.check_output(f"ifconfig {interface_name}", shell=True).decode()
        oldMac = re.search("ether(.*?)txqueuelen", ifconfigResult).group(1).strip()
        # Change MAC address
        subprocess.check_output(f"ifconfig {interface_name} down", shell=True)
        subprocess.check_output(f"ifconfig {interface_name} hw ether {newMac}", shell=True)
        subprocess.check_output(f"ifconfig {interface_name} up", shell=True)
        print(Fore.LIGHTGREEN_EX + f" [SUCCESS] MAC address successfully changed to: {newMac}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + " [WARNING] An error occurred while changing MAC address." + Style.RESET_ALL)
    input("Press Enter to continue...")
    clear_screen()

def display_menu():
    stdout.write(Fore.RED + arts.mac_address)
    stdout.write(Fore.LIGHTCYAN_EX + arts.changer)
    stdout.write(Fore.RED + arts.dev + Fore.LIGHTMAGENTA_EX)
    stdout.write(Fore.LIGHTMAGENTA_EX + "\n" + "[1]" + Fore.LIGHTCYAN_EX + " Change MAC Address" + "\n")
    stdout.write(Fore.LIGHTMAGENTA_EX + "[2]" + Fore.LIGHTCYAN_EX + " Show Current MAC Address" + "\n")
    stdout.write(Fore.LIGHTMAGENTA_EX + "[3]" + Fore.LIGHTCYAN_EX + " Exit" + "\n" + "\n")

def show_current_mac():
    try:
        # Check the network interface name (You can customize this based on your system)
        interface_name = "eth0"
        # Check the current MAC address
        ifconfigResult = subprocess.check_output(f"ifconfig {interface_name}", shell=True).decode()
        current_mac = re.search("ether(.*?)txqueuelen", ifconfigResult).group(1).strip()
        print(Fore.LIGHTGREEN_EX + f" [SUCCESS] Current MAC Address: {current_mac}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + " [WARNING] An error occurred while retrieving current MAC address." + Style.RESET_ALL)
    input("Press Enter to continue...")
    clear_screen()

def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def main():
    while True:
        clear_screen()
        display_menu()
        choice = input(Fore.LIGHTCYAN_EX + "Enter your choice: " + Fore.LIGHTGREEN_EX)
        if choice == "1":
            mac_changer()
        elif choice == "2":
            show_current_mac()
        elif choice == "3":
            print("Exiting...")
            sys.exit()
        else:
            print(Fore.RED + " [!] Invalid choice. Please enter a valid option." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
