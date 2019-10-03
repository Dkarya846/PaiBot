import cv2
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


global cam, ret, Frame, img, photocount
class CameraApp:
    def Camera(self, cameraWindow,window, name, city):
        global photocount
        
        def mainPage():
            from MainLayoutClass import MainLayout
            frame= Frame(cameraWindow, width=480,height=720)
            frame.pack(fill="both", expand=True)
            mainFrame = MainLayout()
            mainFrame.callMain(frame, window, name, city)


        photocount=0
        if cv2.VideoCapture(0).isOpened():
            cam = cv2.VideoCapture(0)
        else:
            cam = cv2.VideoCapture()
            cam.open("https://192.168.1.101:8080/video")

        window.title("PaiBot Camera")
        backbtn = Button(cameraWindow, text="Back", font=("Yatra One",10), activebackground="#163A54", bd=0, command=mainPage, bg="#163A54")
        backbtn.place(x=0,y=690)

        def captureCamera():
            global photocount
            photo = Image.fromarray(cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB))
            photo.save("Photos/Photo"+str(photocount)+".jpg")
            photo.show()
            photocount+=1


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
                    messagebox.showerror("Camera Error","Camera Disconnected")
                    exit(0)
            else :
                cameraWindow.withdraw()
                messagebox.showerror("Camera Error","Camera Is Not connected")
                exit(0)
            if cam.isOpened():    
                cameraWindow.after(5, getVideo)


        #cameraWindow = Tk()
        #cameraWindow.geometry("480x720")
        cameraWindow.config(bg="#163A54")
        #cameraWindow.resizable(False, False)
        cameraLabel = Label(cameraWindow, width=460, height=640, bg="#163A54")
        cameraLabel.place(x=8, y=0)
        cameraBtnImg = PhotoImage(file="Camera/Camera.png")
        cameraButton = Button(cameraWindow, bd=0, image=cameraBtnImg, bg="#163A54", activebackground="#163A54",
                            command=captureCamera)
        cameraButton.image=cameraBtnImg
        cameraButton.place(x=200, y=650)
        getVideo()
        #cameraWindow.mainloop()
