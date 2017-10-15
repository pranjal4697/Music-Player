import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3,TIT2

root=Tk()
audio=ID3()
#Creating a window
root.minsize(400,400)
#making a list for songs
listofsongs=[]
realnames=[]
index=0

def directorychooser():
	directory=askdirectory()
	#changing current directory to the directory chossen by the user
	os.chdir(directory)
	#Adding files to the listofsongs
	for files in os.listdir(directory):
		if(files.endswith(".mp3")):
			realdir=os.path.realpath(files)
			audio=ID3(realdir)
			realnames.append(audio["TIT2"].text[0])
			listofsongs.append(files)

	#Initializing pygame
	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[0])
	pygame.mixer.music.play()

directorychooser()
#Working on GUI
#Giving label
label=Label(root,text="BeatBox")
label.pack()

listbox= Listbox(root)
listbox.pack()

realnames.reverse()

#Inserting songs in the listbox
for items in realnames:
	listbox.insert(0,items)

realnames.reverse()

nextbutton= Button(root,text='Next Song')
nextbutton.pack()

previousbutton= Button(root,text='Previous Song')
previousbutton.pack()

stopbutton= Button(root,text='Stop Music')
stopbutton.pack()




root.mainloop()