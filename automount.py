import os
import time

# Give the USB subsystem a few extra seconds to recognize the drive
time.sleep(5)

def mount_drive(device):
    # systemd runs as root, so sudo is not needed
    os.system(f"mount {device} /mnt/media")

os.system("fdisk -l")
print("fdisk command run")

if os.path.exists("/dev/sda1"):
    mount_drive("/dev/sda1")
    print("sda1 has mounted")
elif os.path.exists("/dev/sdb1"):
    mount_drive("/dev/sdb1")
    print("sdb1 has mounted")
else:
    print("Neither sda1 nor sdb1 were found.")
