from pygame import * 
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

root=Tk()
root.title('Music Player')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=45)
playlist.grid(columnspan=5)

os.chdir(r'D:\movies\songs')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)


playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('arial',18),bg="DodgerBlue2",fg="white",padx=9,pady=9)
playbtn.grid(row=1,column=0)

playbtn=Button(root,text="Pause",command=pausesong)
playbtn.config(font=('arial',18),bg="DodgerBlue2",fg="white",padx=9,pady=9)
playbtn.grid(row=1,column=1)

playbtn=Button(root,text="Stop",command=stopsong)
playbtn.config(font=('arial',18),bg="DodgerBlue2",fg="white",padx=9,pady=9)
playbtn.grid(row=1,column=3)

playbtn=Button(root,text="Resume",command=resumesong)
playbtn.config(font=('arial',18),bg="DodgerBlue2",fg="white",padx=9,pady=9)
playbtn.grid(row=1,column=2)

mainloop()