from tkinter import *
import os
import time
from RegisterPage import Register
from tkinter import messagebox


mainWin = Tk()
mainWin.geometry("480x720")
mainWin.resizable(False, False)
mainWin.iconbitmap("PaiBot.ico")
mainWin.title("PaiBot")
mainWin.config(bg="#163A54")

def logInPage():
    from LogInPage import LogIn
    frame= Frame(mainWin, width=480,height=720)
    frame.pack(fill="both", expand=True)
            
    logInFrame = LogIn()
    logInFrame.logIn(frame, mainWin)


t_end = time.time() + 4 * 1

registerimg = PhotoImage(file="LoadingLogo.png")
register = Label(mainWin, image=registerimg, bg="#163A54")
register.image = registerimg
register.place(x=35, y=25)

greet2 = Label(mainWin, text="Loading...", bg="#163A54", fg="White", font=("Agency FB", 30, "bold"))
greet2.place(x=150, y=520)
"""
btn1 = Button(mainWin,text="  Proceed  ",bg="#163A54", fg="White",font=("Agency FB", 20))
btn1.place(x=360, y=645)"""

# mimic an animated GIF displaying a series of GIFs
# an animated GIF was used to create the series of GIFs 
# with a common GIF animator utility
imageList = ["Loading/ld1.png", "Loading/ld1_(2).png", "Loading/ld1_(3).png",
             "Loading/ld1_(4).png", "Loading/ld1_(5).png", "Loading/ld1_(6).png",
             "Loading/ld1_(7).png", "Loading/ld1_(8).png", "Loading/ld1_(9).png",
             "Loading/ld1_(10).png", "Loading/ld1_(11).png", "Loading/ld1_(12).png",
             "Loading/ld1_(13).png", "Loading/ld1_(14).png", "Loading/ld1_(14).png",
             "Loading/ld1_(15).png", "Loading/ld1_(16).png", "Loading/ld1_(17).png",
             "Loading/ld1_(18).png", "Loading/ld1_(19).png", "Loading/ld1_(20).png",
             "Loading/ld1_(21).png", "Loading/ld1_(22).png", "Loading/ld1_(23).png",
             "Loading/ld1_(24).png", "Loading/ld1_(25).png", "Loading/ld1_(26).png",
             "Loading/ld1_(27).png", "Loading/ld1_(28).png", "Loading/ld1_(29).png",
             "Loading/ld1_(30).png", "Loading/ld1_(31).png", "Loading/ld1_(32).png",
             "Loading/ld1_(33).png", "Loading/ld1_(34).png", "Loading/ld1_(35).png",
             "Loading/ld1_(36).png", "Loading/ld1_(37).png", "Loading/ld1_(38).png",
             "Loading/ld1_(39).png", "Loading/ld1_(40).png", "Loading/ld1_(41).png",
             "Loading/ld1_(42).png", "Loading/ld1_(43).png", "Loading/ld1_(44).png",
             "Loading/ld1_(45).png", "Loading/ld1_(48).png", "Loading/ld1_(49).png", ]
# extract width and height info
photo = PhotoImage(file=imageList[0])
width = photo.width()
height = photo.height()
canvas = Canvas(width="400", height="300", bg="#163A54", highlightbackground="#163A54")
canvas.place(x=90, y=200)
# create a list of image objects
giflist = []



for imageFile in imageList:
    photo = PhotoImage(file=imageFile)
    giflist.append(photo)
# loop through the gif image objects for a while
try:
    while time.time() < t_end:
        for gif in giflist:
            canvas.create_image(width / 2.0, height / 2.0, image=gif)
            canvas.update()
            time.sleep(0.005)
            canvas.delete(ALL)
except RuntimeError as e:
    messagebox.showerror("Error", (e))
except Exception as e:
    messagebox.showerror("Error", str(e))
photo1 = PhotoImage(file="Loading/ld1_(49).png")
width = photo1.width()
height = photo1.height()
canvas = Canvas(width="400", height="300", bg="#163A54", highlightbackground="#163A54")
canvas.create_image(width / 2.0, height / 2.0, image=photo1)
canvas.place(x=90, y=200)

greet3 = Label(mainWin, text="Let's Go..", bg="#163A54", fg="White", font=("Agency FB", 30, "bold"))
greet3.place(x=150, y=520)


btn1 = Button(mainWin, text="  Proceed  ", bg="#163A54", fg="White", font=("Agency FB", 15), command=logInPage)
btn1.place(x=360, y=645)

mainWin.mainloop()
