import socket
import os
import gui


def ping(_server_ip):
    rep = os.system('ping ' + _server_ip)  # Ping ip adress

    # Give output
    if rep == 0:
        return True
    else:
        return False

    return


def getIP(_url):
    socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket

    try:
        server_ip = socket.gethostbyname(_url)  # Get ip adress from url
    except socket.gaierror:
        server_ip = 'Error: IP not found'

    return server_ip


def getUserInput():

    url = gui.urlEntered.get()

    serverIP = getIP(url)

    statusMsg = ''

    if ping(serverIP):
        statusMsg = url + ' is responding'
    elif not ping(serverIP):
        statusMsg = url + ' is not responding'
    else:
        statusMsg = None

    gui.updateInfo(statusMsg, url, serverIP)
