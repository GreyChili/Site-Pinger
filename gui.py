import tkinter as tk
import ping


def updateInfo(newStatus, newURL, newIP):

    if type(newStatus) == str:
        status.configure(text=newStatus)
    else:
        status.configure(text='STATUS')

    if type(newURL) == str:
        siteURL.configure(text='URL: ' + newURL)
    else:
        siteURL.configure(text='URL')

    if type(newIP) == str:
        siteIP.configure(text=newIP)
    else:
        siteIP.configure(text='IP')


# Create a window
window = tk.Tk()
window.title('Site Pinger')
window.minsize(250, 125)

title = tk.Label(window, text='ENTER URL')  # Title
title.pack()
urlEntered = tk.Entry(window)  # URL Entry
urlEntered.pack()
urlEntered.focus_set()
pingBtn = tk.Button(window, text='PING', command=ping.Main)  # Button
pingBtn.pack()
status = tk.Label(window, width=25, text='STATUS')  # Status of site
status.pack()
siteURL = tk.Label(window, width=25, text='URL')  # URL of site
siteURL.pack()
siteIP = tk.Label(window, width=25, text='IP')  # IP of site
siteIP.pack()

window.mainloop()
