import socket
from IPy import IP
import os

os.system('clear')

def scan(target):
    converted_ip = check_ip(target)
    print('\n' +  '[ Scanning Faggot.. I MEAN TARGET!!] ' + str(target))

    for port in range(1,8080):
       scan_port(converted_ip, port)



def check_ip(ip):
     try:
         IP(ip)
         return(ip)
     except ValueError:
         return socket.gethostbyname(ip)


def get_banner(s):
    return  s.recv(1024)



def scan_port(ipaddress, port):
  try:
      sock = socket.socket()
      sock.settimeout(0.5)
      sock.connect((ipaddress, port)) 
      try:
          banner = get_banner(sock)
          print('Port' + str(port) + ' : ' + str(banner))
      except:
              print('[+] Open port' + str(port))
  except:
         pass


targets = input('[x] ENTER TARGET/TARGETS YOU WANT TO SCAN: ')
port_num = input('Enter Number of ports that you want to scan: ')
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
     scan(targets)

