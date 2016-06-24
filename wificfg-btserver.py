import subprocess
import re

output = subprocess.check_output(['sudo', 'iwlist', 'wlan0', 'scan'])
lines = output.splitlines()
for line in lines:
    match = re.search("^\s+ESSID:\"(.+)\"$", line)
    if match:
        print match.group(1)
