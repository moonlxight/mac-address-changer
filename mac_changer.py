# TR: Bu dosya "sudo" yetkileriyle çalıştırılması tavsiye edilir. Aksi takdirde hata verebilir.
# EN: It is recommended that you run this file with "sudo" permissions. Or else you might get an error.

import random
import subprocess
import re

charList = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
newMac = ""

for i in range(6):
    newMac += random.choice(charList) + random.choice(charList)
    if i < 5:
        newMac += ":"

ifconfigResult = subprocess.check_output("ifconfig eth0", shell=True).decode()
oldMac = re.search("ether(.*?)txqueuelen",ifconfigResult).group(1).strip()

subprocess.check_output("ifconfig eth0 down", shell=True)

#subprocess.check_output("ifconfig eth0 hw ether "+newMac, shell=True) # Yöntem / Method #1
subprocess.check_output("ip link set dev eth0 address "+newMac, shell=True) # Yöntem / Method #2

subprocess.check_output("ifconfig eth0 up", shell=True)

print("Old Mac Address : ", oldMac)
print("New Mac Address : ", newMac)

