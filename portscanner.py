# communication with other machines with TCP/UDP
import socket

# iterate through every port for a target
def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(targets, port)

def scan_port(ipaddress, port):

    try:
        # whenever we create some connection we need to initiate a socket
        sock = socket.socket()

        # to connect we need a target ip address and port number
        # this will either succeed i.e. connect (port is open) to the port or not (port is closed)
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass


targets = input("[*] Enter Targets To Scan(Split them by ,): ")
ports = int(input("[*] Enter How Many Ports To Scan: "))

# If multiple targets call scan on each
if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)