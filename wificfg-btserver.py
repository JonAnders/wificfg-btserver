import subprocess
import re

def scan_wifi():
    output = subprocess.check_output(['sudo', 'iwlist', 'wlan0', 'scan'])
    lines = output.splitlines()
    networks = []
    for line in lines:
        match = re.search("^\s+ESSID:\"(.+)\"$", line)
        if match:
            networks.append(match.group(1))

    return networks

nets = scan_wifi()
for net in nets:
    print "> " + net
