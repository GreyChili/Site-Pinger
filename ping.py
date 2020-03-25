import tkinter as tk
import socket
import sys
import os

url = ''
server_ip = ''
rep = None
s = None



def ping(_server_ip, _url):
    rep = os.system('ping ' + _server_ip)  # Ping ip adress

    # Give output
    if rep == 0:
        statusMsg = _url + ' is up'
    else:
        statusMsg = _url + ' is down'

    status.configure(text=statusMsg)
    print(statusMsg)

    

def getIP():
    status.configure(text='STATUS')
    url = urlEntered.get()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
    server_ip = socket.gethostbyname(url)  # Get ip adress from url

    ping(server_ip, url) # Ping


# Create a window
window = tk.Tk()
window.title('Site Pinger')
window.minsize(250, 100)

title = tk.Label(window, text='ENTER URL') # Title
title.pack()
urlEntered = tk.Entry(window) # URL Entry
urlEntered.pack()
pingBtn = tk.Button(window, text='PING', command=getIP) # Button
pingBtn.pack()
status = tk.Label(window, width=20, text='STATUS') # Status of site
status.pack()

window.mainloop()
