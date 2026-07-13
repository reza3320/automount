**To mount the Storage units automatically for Linux(Debian) servers**

**First step:**
Choose a permanent directory for placing the Automount.py
For example: ```/etc/automount/ ```


Go to ```/lib/systemd/system``` Directory.


**Step 2:**
We are going to make a system service.


Make a file named : ```automount.service```
Write the code bellow down in **automount.service**:


```
[Unit]
Description=Automount Python Service
After=local-fs.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/bin/python3 /opt/automount/automount.py

[Install]
WantedBy=multi-user.target
```

```cp automount.service /etc/systemd/system/automount.service```
```chmod 644 /lib/systemd/system/automount.service```
```chmod +x /etc/automount/automount.py```


**Step3:**
Now you can start and make the mounter restartable with codes bellow:


``` sudo systemctl deamon-reaload```
``` sudo systemctl start automount```
``` sudo systemctl enable automount```
```sudo systemctl restart automount```
