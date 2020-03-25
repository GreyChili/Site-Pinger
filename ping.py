import socket
import os
import gui


def ping(_server_ip, _url):
    rep = os.system('ping ' + _server_ip)  # Ping ip adress

    # Give output
    if rep == 0:
        gui.updateStatus(_url + ' is responding')
    else:
        gui.updateStatus(_url + ' is not responding')

    return


def getIP():
    gui.updateStatus(None)
    url = gui.urlEntered.get()

    socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket

    try:
        server_ip = socket.gethostbyname(url)  # Get ip adress from url
    except socket.gaierror:
        gui.updateStatus('Error: IP not found')

    ping(server_ip, url)  # Ping

def updateSiteInfo():
    pass