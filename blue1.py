# Import required packages
import schedule
import time
import bluetooth
import ctypes
import keyboard

scan = bluetooth.discover_devices(lookup_names=True)
for i,j in scan:
    print(i,":",j)
inputBdaddr = input("copy and paste address you want to setup:")
	
# Variable to find whether the
# given bluetooth uuid is
# present in the discovered devices
passed = True
while True:
    scan = bluetooth.discover_devices()
    print(scan)
    if inputBdaddr in scan:
        passed = True
    else:
        passed = False
    print(passed)
    if not passed:
        if ctypes.windll.user32.LockWorkStation()==0:
            ctypes.windll.user32.LockWorkStation()
