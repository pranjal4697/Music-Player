import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3,TIT2
from tkinter.font import Font
import matplotlib



pygame.init()
root=Tk()

audio=ID3()
text=Text(root)
helv=Font(family="Helvetica",size=100,weight="bold")
text.configure(font=helv)
root.wm_title("boomBOX")
#Creating a window
root.minsize(500,500)
#making a list for songs
listofsongs=[]
realnames=[]
index=0
ctr=0
numberofsongs=0

str=StringVar()
songlabel=Label(root,textvariable=str,width=50)

def pausesong(event):
	global ctr
	ctr+=1
	if(ctr%2==0):
		pygame.mixer.music.unpause()
	else:
		pygame.mixer.music.pause()

def nextsong(event):
	global index
	index+=1
	if(index<numberofsongs):
		pygame.mixer.music.load(listofsongs[index])
		pygame.mixer.music.play()
	else:
		index=0;
		pygame.mixer.music.load(listofsongs[index])
		pygame.mixer.music.play()
	updatelabel()
	
	

def previoussong(event):
	global index
	index-=1
	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()
	updatelabel()

def stopsong(event):
	pygame.mixer.music.stop()
	str.set("")
	return songlabel

def playsong(event):
	pygame.mixer.music.play()

def mutesong(event):
	vol.set(0)

def updatelabel():
	global index
	global songlabel
	str.set(realnames[index])
	return songlabel


def directorychooser():
	directory=askdirectory()
	#changing current directory to the directory chossen by the user
	os.chdir(directory)
	#Adding files to the listofsongs
	for files in os.listdir(directory):
		try:
			if(files.endswith(".mp3") or files.endswith(".flac")):
				realdir=os.path.realpath(files)
				audio=ID3(realdir)
				realnames.append(audio["TIT2"].text[0])
				listofsongs.append(files)
		except:
			print("Can't find the metadata for "+files)
	noOfSongs()		


	#Initializing pygame
	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[0])
	updatelabel()
	pygame.mixer.music.play()

def show_value(self):
    i = vol.get()
    pygame.mixer.music.set_volume(i)

def noOfSongs():
	global numberofsongs
	if(listofsongs==[]):
		print("No Songs Found")
	else:
		for i in listofsongs:
			numberofsongs+=1

listbox=Listbox(root,selectmode=MULTIPLE,width=100,height=30,bg="coral",fg="black")
listbox.pack(fill=X)

vol=Scale(root,from_=40,to=0,orient=HORIZONTAL,resolution=20,command=show_value)   
vol.place(x=60,y=520)
vol.set(10)

directorychooser()
#Working on GUI
#Giving label

label=Label(root,text="BoomBox",font="helv")
label.pack()

realnames.reverse()

#Inserting songs in the listbox
for items in realnames:
	listbox.insert(0,items)

realnames.reverse()



framemiddle =Frame(root,width=250,height=30)
framemiddle.pack()


framedown =Frame(root,width=400,height=300)
framedown.pack()

mutebutton = Button(framedown,text="Mute", activebackground="red")
mutebutton.pack(side=LEFT)


previousbutton= Button(framedown,text="◄◄", activebackground="green")
previousbutton.pack(side=LEFT)

stopbutton= Button(framedown,text="■", activebackground="red" )      #has no functionality
stopbutton.pack(side=LEFT)

pausebutton = Button(framedown,text="►/║║")
pausebutton.pack(side=LEFT)

nextbutton= Button(framedown,text="►►", activebackground="green")
nextbutton.pack(side=LEFT)

playbutton=Button(framedown,text="►")
playbutton.pack(side=LEFT)







mutebutton.bind("<Button-1>",mutesong)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",previoussong)
stopbutton.bind("<Button-1>",stopsong)
playbutton.bind("<Button-1>",playsong)
pausebutton.bind("<Button-1>",pausesong)
songlabel.pack()






root.mainloop()