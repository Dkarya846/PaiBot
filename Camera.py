import cv2
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from sys import *
import datetime


global cam, ret, Frame, img, photocount


photocount=0
try:
    files=open('Photos/PhotoCount.camera', 'r')
    photocount=int(files.readline())
    files.close()
except FileNotFoundError:
        with open("Photos/PhotoCount.camera",'w') as f:
            f.write('%d' % photocount)
if cv2.VideoCapture(0).isOpened():
    cam = cv2.VideoCapture(0)
else:
    cam = cv2.VideoCapture()
    cam.open("https://192.168.1.101:8080/video")

#window.title("PaiBot Camera")

def captureCamera():
    global photocount
    photo = Image.fromarray(cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB))
    photo.save("Photos/IMG"+str(datetime.datetime.now().strftime("%Y%m%d"))+str(photocount)+".jpg")
    photo.show()
    photocount+=1
    with open('Photos/PhotoCount.camera', 'w') as f:
        f.write('%d' % photocount)


def getVideo():
    if cam.isOpened():
        global img
        global ret, Frame
        ret, Frame = cam.read()
        try:
            images = Image.fromarray(cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB))
            img = ImageTk.PhotoImage(images)
            cameraLabel.config(image=img)
        except cv2.error as e:
            cameraWindow.withdraw()
            messagebox.showerror("Camera Error","Camera Disconnected")
            exit(0)
    else :
        cameraWindow.withdraw()
        messagebox.showerror("Camera Error","Camera Is Not connected")
        exit(0)
    if cam.isOpened():    
        cameraWindow.after(5, getVideo)


cameraWindow = Tk()
cameraWindow.geometry("480x720")
cameraWindow.config(bg="#163A54")
cameraWindow.title("PaiBot Camera")
cameraWindow.resizable(False, False)
cameraLabel = Label(cameraWindow, width=460, height=640, bg="#163A54")
cameraLabel.place(x=8, y=0)
cameraBtnImg = PhotoImage(file="Camera/Camera.png")
cameraButton = Button(cameraWindow, bd=0, image=cameraBtnImg, bg="#163A54", activebackground="#163A54",
                    command=captureCamera)
cameraButton.image=cameraBtnImg
cameraButton.place(x=200, y=650)
backbtn = Button(cameraWindow, text="Exit", font=("Yatra One",10), activebackground="#163A54", bd=0, command=quit, bg="#163A54")
backbtn.place(x=0,y=690)
getVideo()
cameraWindow.mainloop()