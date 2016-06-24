output = subprocess.check_output(['iwlist', 'wlan0', 'scan'])
print output
