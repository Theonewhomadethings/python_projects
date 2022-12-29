'''
GUI Youtube Video Downloader
Basic tkinkter GUI
Input: any youtube link
Input: desired user path for location of video
Output: mp4 of youtube video in desired location
'''
from os import path
import tkinter
from tkinter import *
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

'''
Path selecter function.
 Allows user to select a path from their file explorer.
'''
def selectPath():
    path = filedialog.askdirectory()
    pathLabel.config(text = path)

'''
File downloader function.
Obtains the link.
Obtains users path.
Downloads video.
'''
def downloadFile():
    getLink = linkField.get()
    userPath = pathLabel.cget("text")
    mp4Video = YouTube(getLink).streams.get_highest_resolution().download()
    vidClip = VideoFileClip(mp4Video)
    vidClip.close()
    shutil.move(mp4Video, userPath)
    screen.title("Download Comeplete! Download Another File...")


#UI
screen = Tk()
title = screen.title("Youtube downloader")
canvas = Canvas(screen, width = 500, height=500)
canvas.pack()

logoImage = PhotoImage(file = 'ytLogo1.png') #logo 
logoImageResize = logoImage.subsample(4, 4) #logorezise
canvas.create_image(250, 80, image = logoImageResize)

#link field!
linkField = Entry(screen, width = 50)
linkLabel = Label(screen, text = "Enter Download link: ")

pathLabel = Label(screen, text = "Select Path For Download: ", font = ("Arial", 15))
selectButton = Button(screen, text = "Select", command=selectPath )

#add to window
canvas.create_window(250, 280, window=pathLabel)
canvas.create_window(250, 330, window = selectButton)

#add widgets to window!
canvas.create_window(250, 180, window=linkLabel)
canvas.create_window(250, 210, window=linkField)

#download buttons
downloadButton = Button(screen, text = "Download File", command=downloadFile)

canvas.create_window(250, 390, window=downloadButton)

screen.mainloop()

