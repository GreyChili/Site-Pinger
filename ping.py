import socket
import os
import gui

url = ''
server_ip = ''
rep = None
s = None



def ping(_server_ip, _url):
    rep = os.system('ping ' + _server_ip)  # Ping ip adress

    # Give output
    if rep == 0:
        updateStatus(_url + ' is responding')
    else:
        updateStatus(_url + ' is not responding')

    

def getIP():
    updateStatus(None)
    url = gui.urlEntered.get()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket

    try:
        server_ip = socket.gethostbyname(url)  # Get ip adress from url
    except socket.gaierror:
        updateStatus('Error: IP not found')

    ping(server_ip, url) # Ping

def updateStatus(statusMsg):
    if type(statusMsg) == str:
        gui.status.configure(text=statusMsg)
    else:
        pass

    return
