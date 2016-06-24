import subprocess
import re

output = subprocess.check_output(['iwlist', 'wlan0', 'scan'])
lines = output.splitlines()
for line in lines:
    if re.search("^\s+ESSID", line):
        print line
