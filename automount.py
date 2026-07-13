import os
import time

# Wait for the USB subsystem
time.sleep(5)

# Replace this with the actual UUID you got from the blkid command
DRIVE_UUID = "a1b2c3d4-e5f6-7890"

print("Attempting to mount by UUID...")

# Tell Linux to find the drive by its ID and mount it
# Note: systemd runs as root, so sudo is not needed here
exit_code = os.system(f"mount UUID={DRIVE_UUID} /mnt/media")

if exit_code == 0:
    print("Drive successfully mounted!")
else:
    print("Failed to mount the drive.")
