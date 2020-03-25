import tkinter as tk
import ping

# Create a window
window = tk.Tk()
window.title('Site Pinger')
window.minsize(250, 100)

title = tk.Label(window, text='ENTER URL') # Title
title.pack()
urlEntered = tk.Entry(window) # URL Entry
urlEntered.pack()
pingBtn = tk.Button(window, text='PING', command=ping.getIP) # Button
pingBtn.pack()
status = tk.Label(window, width=20, text='STATUS') # Status of site
status.pack()

window.mainloop()