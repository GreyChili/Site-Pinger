import tkinter as tk
import socket
import sys
import os

url = ''
server_ip = ''
rep = None
s = None



def ping():
    rep = os.system('ping ' + server_ip)  # Ping ip adress

    # Give output
    if rep == 0:
        status.configure(text=url + ' is up')
    else:
        status.configure(text=url + ' is down')

def getIP():
    print('Getting IP')
    if url != '':
        print(url)
    else:
        print('No URL')

    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
    server_ip = socket.gethostbyname(url)  # Get ip adress from url
    ping()


# Create a window
window = tk.Tk()
window.title('Site Pinger')
window.minsize(250, 100)

title = tk.Label(window, text='Enter URL') # Title
urlEntered = tk.Entry(window) # URL Entry
pingBtn = tk.Button(window, text='Ping', command=getIP) # Button
status = tk.Label(window, text='Status') # Status of site

title.pack()
urlEntered.pack()
url = urlEntered.get()
pingBtn.pack()
status.pack()

window.mainloop()
