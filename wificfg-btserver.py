import subprocess

output = subprocess.check_output(['iwlist', 'wlan0', 'scan'])
lines = output.splitlines()
print lines.count()
