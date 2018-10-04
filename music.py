import os
from tkinter.filedialog import askdirectory
import pygame
import PIL.Image

from tkinter import *
root =Tk()
root.minsize(1600,800)
root.title("Music Player")
listofsongs = []
index = 0
event=" "
def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
def stopsong(event):
    pygame.mixer.music.pause()
def resumesong(event):
    pygame.mixer.music.unpause()
def directorychooser():
    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            #realdir = os.path.realpath(files)
            #audio = ID3(realdir)
            #realnames.append(audio['TIT2'].text[0])

            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
directorychooser()
label = Label(root,font=('arial', 40, 'bold'),text = 'Music Player')
label.pack()
listbox = Listbox(root, bg="turquoise1", width= 200, height=10, bd=20)
listbox.pack()
listofsongs.reverse()
#realnames.reverse()
for items in listofsongs:
    listbox.insert(0,items)
listofsongs.reverse()
#realnames.reverse()

"""nextbutton = Button(root, text = 'Next Song')
nextbutton.pack()
previousbutton = Button(root, text = 'Previous Song')
previousbutton.pack()
stopbutton = Button(root,text = 'Pause Music')
stopbutton.pack()
resumebutton = Button(root,text = 'Resume Music')
resumebutton.pack()
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
resumebutton.bind("<Button-1>",resumesong)"""
f2= Frame(root, width=1600, height=800, bg="powder blue", relief=SUNKEN)
f2.pack()
f1= Frame(root, width=1600, height=800, bg="powder blue", relief=SUNKEN)
f1.pack()
f3= Frame(root, width=1600, height=800, bg="powder blue", relief=SUNKEN)
f3.pack()
btn7=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="<", bg="powder blue", command=lambda:prevsong(event)).grid(row=2, column=0)
btn7=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="||", bg="powder blue", command=lambda:stopsong(event)).grid(row=2, column=1)
btn7=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="/\ ", bg="powder blue", command=lambda:resumesong(event)).grid(row=2, column=2)
btn7=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=">", bg="powder blue", command=lambda:nextsong(event)).grid(row=2, column=3)

btn8=Button(f1, width= 19, height=2, bd=8, fg="black", font=('arial', 20, 'bold'), text="X", bg="powder blue", command=quit).grid(row=3, column=0)

"""fp = open("1.JPG","rb")
img = PIL.Image.open(fp)

w=Label(f3, bd=8, image=img)
w.pack()"""


root.mainloop()