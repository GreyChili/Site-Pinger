import socket
import os
import updateGui
import siteInfo as info
import gui

url = ''
server_ip = ''
site = None
rep = None


def ping(_server_ip, _url):
    rep = os.system('ping ' + _server_ip)  # Ping ip adress

    # Give output
    if rep == 0:
        updateGui.updateStatus(_url + ' is responding')
    else:
        updateGui.updateStatus(_url + ' is not responding')

    return


def getIP():
    global url
    global server_ip
    updateGui.updateStatus(None)
    url = gui.urlEntered.get()

    socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket

    try:
        server_ip = socket.gethostbyname(url)  # Get ip adress from url
    except socket.gaierror:
        updateGui.updateStatus('Error: IP not found')

    ping(server_ip, url)  # Ping
    updateSiteInfo() # Update site info on GUI

def updateSiteInfo():
    global site
    site = info.Website(url, server_ip)