import socket
import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Ping a website by URL')
parser.add_argument('-u', '--url', type=str, metavar='', required=True, help='URL to ping')
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
server_ip = socket.gethostbyname(args.url) # Get ip adress from url
rep = os.system('ping ' + server_ip) # Ping ip adress

# Give output
if rep == 0:
    print('\n\n%s is up' %server_ip)
else:
    print('server is down')
