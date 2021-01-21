import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from PIL import Image
from PIL import ImageTk
import os
from tkinter import filedialog
import urllib
from urllib.request import urlopen
import requests
##import cv2
import socket
from tkinter import messagebox
from tkinter import PhotoImage
##import sys
##https://youtu.be/rVZOFU85y0c
def convert_next(event = 0):
    global win
    global b1
    b1 = front(win)
def isConnected():
    url = "http://www.kite.com"
    timeout = 5
    try:
	    request = requests.get(url, timeout=timeout)
	    return True
    except (requests.ConnectionError, requests.Timeout) as exception:
	    return False
win = tk.Tk()
win.title("YouTube Downloader")
win.state("zoomed")
##win.wm_iconbitmap(r'F:\chunnu\python pro\youtube\icon.ico')
##win.iconphoto(True, PhotoImage(file="F:\chunnu\python pro\youtube\app icon.png"))
##win.iconbitmap(os.path.join(sys.path[0], "/data/html/icon.ico"))

width, height = win.winfo_screenwidth(), win.winfo_screenheight()
load = Image.open(r'F:\chunnu\python pro\youtube\bg3.png')
if load.size != (width, height):
    load = load.resize((width, height), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = ttk.Label(win,image = render)
img.place(x = 0,y = 0)

class transfer:
    def __init__(self):
        global b1
        global win
        self.file_type = b1.file_combobox.get()
        self.file_url = b1.url_var.get()
        self.frame = b1.label_frame
        if self.file_type == 'Video':
            self.frame.after(1000, self.frame.destroy)
            b3 = video_download(win,self.file_url,)
        else:
            self.frame.after(1000, self.frame.destroy)
            b3 = audio(win,self.file_url)

class video_download:
    def __init__(self,win,url):
        self.win = win
        self.url = url
        global b1
        self.label_frame = ttk.LabelFrame(win)
        self.label_frame.place(x = 700,y = 300,anchor = 'center') 
        self.please = tk.Label(self.label_frame,text =  'Downloading please wait')
        self.please.grid(row = 0, column = 0)
        self.btn = True
        if isConnected():
            try:
                self.obj = YouTube(self.url)
            except KeyError as e:
                messagebox.showerror("Connection error", "Check your connection")
                b1 = front(win)
                self.btn = False
            except urllib.error.URLError as e:
                messagebox.showerror("Connection error", "Check your connection")
                b1 = front(win)
                self.btn = False

        if isConnected():
            try:
                self.title = self.obj.title
                self.title_label = tk.Label(self.label_frame ,text = self.title)
                self.title_label.grid(row = 1,column = 0)
                self.precessing_label = tk.Label(self.label_frame,text = "Downloading...")
                self.precessing_label.grid(row = 2,column = 0)
            except AttributeError:
                messagebox.showerror("Connection error", "Check your connection")
                b1 = front(win)
                self.btn = False
        else:
            messagebox.showerror("Connection error", "Check your connection")
            b1 = front(win)
            self.btn = False
        
        if isConnected():    
            self.path = filedialog.askdirectory()
        try:
            os.chdir(self.path)
        except OSError as e:
            b1 = front(win)
            self.btn = False
        except AttributeError:
            b1 = front(win)
            self.btn = False

        if isConnected():
            self.stream = self.obj.streams.first()
            self.stream.download(self.path)
##            self.precessing_label.after(1000, self.precessing_label.master.destroy)
            self.precessing_label2 = tk.Label(self.label_frame,text ='Downloaded')
            self.precessing_label2.grid(row = 3,column = 0)

        else:
            messagebox.showerror("Connection error", "Check your connection")
            b1 = front(win)
            self.btn = False
        if self.btn is True:
            self.convert_next = tk.Button(self.label_frame,text = 'Convert Next', command = convert_next )
            self.convert_next.grid(row = 4,column = 0)

class audio:
    def __init__(self,win,url):
        self.win = win
        self.url = url
        global b1
        self.btn = True
        self.label_frame = ttk.LabelFrame(win)
        self.label_frame.place(x = 700,y = 300,anchor = 'center') 
        self.please = tk.Label(self.label_frame,text =  'Downloading please wait')
        self.please.grid(row = 0, column = 0)
        
        if isConnected():
            try:
                self.obj = YouTube(self.url)
            except KeyError as e:
                messagebox.showerror("Connection error", "Check your connection")
                b1 = front(win)
                self.btn = False
            except urllib.error.URLError as e:
                messagebox.showerror("Connection error", "Check your connection")
                b1 = front(win)
                self.btn = False

        if isConnected():
            try:
                self.title = self.obj.title
                self.title_label = tk.Label(self.label_frame ,text = self.title)
                self.title_label.grid(row = 1,column = 0)
                self.precessing_label = tk.Label(self.label_frame,text = "Downloading...")
                self.precessing_label.grid(row = 2,column = 0)
            except AttributeError:
                messagebox.showerror("Connection error", "Check your connection")
                self.btn = False
        else:
            messagebox.showerror("Connection error", "Check your connection")
            b1 = front(win)
            self.btn = False
        
        if isConnected():
            self.path = filedialog.askdirectory()
        try:
            os.chdir(self.path)
        except OSError as e:
            b1 = front(win)
            self.btn = False
        except AttributeError:
            b1 = front(win)
            self.btn = False

        if isConnected():
            self.stream = self.obj.streams.filter(type = 'audio')
            self.stream.first().download(self.path)
##            self.precessing_label.after(1000, self.precessing_label.master.destroy)
            self.precessing_label2 = tk.Label(self.label_frame,text ='Downloaded')
            self.precessing_label2.grid(row = 3,column = 0)

        else:
            messagebox.showerror("Connection error", "Check your connection")
            b1 = front(win)
            self.btn = False
        if self.btn is True:
            self.convert_next = tk.Button(self.label_frame,text = 'Convert Next', command = convert_next )
            self.convert_next.grid(row = 4,column = 0)

class front:
    def __init__(self,win):
        self.win = win
        self.label_frame = ttk.LabelFrame(win)
        self.label_frame.place(x = 700,y = 300,anchor = 'center')
        self.url_var = tk.StringVar()
        self.url_label = ttk.Label(self.label_frame,text = 'Enter you url : ')
        self.url_label.grid(row = 0, column = 0)
        
        self.url_entrybox = ttk.Entry(self.label_frame,width = 50,textvariable = self.url_var)
        self.url_entrybox.grid(row = 0,column = 1)
        self.url_entrybox.focus()

        self.combobox_label = ttk.Label(self.label_frame,text = 'Select your file type: ')
        self.combobox_label.grid(row = 0, column = 3)
        self.file_combobox = tk.StringVar()
        self.file_combobox = ttk.Combobox(self.label_frame,width = 16,textvariable = self.file_combobox, state = 'readonly')
        self.file_combobox['values'] = ('Video','Audio')
        self.file_combobox.current(0)
        self.file_combobox.grid(row = 0, column = 4)
        self.download_btn = tk.Button(self.label_frame,text = 'Download', command = transfer )
        self.download_btn.grid(row = 4,column = 0)


b1 = front(win)
win.mainloop()