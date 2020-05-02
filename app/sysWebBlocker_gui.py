import threading, subprocess, os
from tkinter import *
import tkinter.messagebox

bgColor = '#1B1837'
appendOutput = open(r'/log.txt', 'a+')

class SysWebBlocker():
    def __init__(self, master):
        mainFrame = Frame(master, bg=bgColor)
        mainFrame.pack(pady=10)

        self.wbUrl = StringVar()
        
        self.lblTitle = Label(mainFrame, text="Sys Website Blocker", font=["Segoe UI", 14, "bold"], bg=bgColor, fg='white')
        self.label = Label(mainFrame, text="Enter the website to block (i.e. 'www.google.com')", bg=bgColor, fg='white')
        self.lblTitle.pack()
        self.label.pack()

        formFrame = Frame(mainFrame, bg=bgColor)
        formFrame.pack(pady=10)
        self.label2 = Label(formFrame, text="URL / Website", bg=bgColor, fg='white')
        self.tbWebUrl = Entry(formFrame, width=40, justify='center', textvariable=self.wbUrl)
        self.btnBlockWeb = Button(formFrame, text="BLOCK", bg='#DD4F42', fg='white', padx=15, pady=15, command=lambda:self.startProc())
        self.label2.pack()
        self.tbWebUrl.pack(ipady=5)
        self.btnBlockWeb.pack(pady=10)

        self.blkDir = "C:\Windows\System32\drivers\etc"

    def startProc(self):
        rWebUrl = self.wbUrl.get()
        t = threading.Thread(target=self.blockWebsite, args=[rWebUrl])
        t.daemon = True
        t.start()
    def blockWebsite(self, rWebUrl):
        print(rWebUrl)
        _blockWeb = subprocess.Popen("echo 127.0.0.1 " + rWebUrl + " >> hosts #sysWebBlockerBETA && ipconfig /flushdns", universal_newlines=True, stdout=appendOutput, stderr=appendOutput, shell=True, cwd=self.blkDir)
        stdout, stderr = _blockWeb.communicate()
        if (_blockWeb.returncode == 0):
            tkinter.messagebox.showinfo("SUCCESS!", "The website " + rWebUrl + " is successfully BLOCKED!")
        else:
            tkinter.messagebox.showerror("EROR!", "An error has occured, the website was not blocked.")
        
root = Tk()
root.configure(bg=bgColor)
root.geometry('450x200')

_sys = SysWebBlocker(root) 

root.mainloop()