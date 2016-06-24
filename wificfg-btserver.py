import subprocess
import re
from bluetooth import *

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "30b5bb9b-b834-44dc-88b3-bb9db508fbca"

advertise_service( server_sock, "wificfg",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
                    )

while True:
    print("Waiting for connection on RFCOMM channel %d" % port)
    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)

    try:
        nets = scan_wifi()
        for net in nets:
            client_sock.send(net + "\n")
    except IOError:
        pass

    print("Disconnected")

    client_sock.close()

server_sock.close()

def scan_wifi():
    output = subprocess.check_output(['sudo', 'iwlist', 'wlan0', 'scan'])
    lines = output.splitlines()
    networks = []
    for line in lines:
        match = re.search("^\s+ESSID:\"(.+)\"$", line)
        if match:
            networks.append(match.group(1))

    return networks
