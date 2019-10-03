from tkinter import *
from Weather import Weather
from MediaPlayer import Media
win1 = Tk()
win1.geometry("480x720")
win1.iconbitmap('PaiBot.ico')

frame = Frame(win1,width=480, height=720)
frame.pack(fill=BOTH,expand=TRUE)

mediaFrame = Media()
mediaFrame.musicPlayer(frame, win1)
win1.mainloop()