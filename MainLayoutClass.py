from datetime import *
import os
from tkinter import *
from requests import *
import webbrowser
from PIL import ImageTk, Image
import time as times
import requests
from tkinter import messagebox
from LogInPage import LogIn
from Weather import Weather
from TBA import TBAClass
from LogInPage import LogIn

                
                      

class MainLayout:
    def callMain(self, win, registerwin, name="User", city="Delhi"):
        try:
            registerwin.title("PaiBot")
           
            def logInPage():
                frame= Frame(win, width=480,height=720)
                frame.pack(fill="both", expand=True)
                        
                logInFrame = LogIn()
                logInFrame.logIn(frame, registerwin)


            def weatherForcast():
                frame = Frame(win,width=480, height=720)
                frame.pack(fill=BOTH,expand=TRUE)
                weatherFrame = Weather()
                weatherFrame.getWeather(frame, registerwin, name, city)
            
            
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&APPID=47657b66139fc2cb733e7566ec239fd1"
            try:
                data = requests.get(url).json()
                temp = data['main']['temp']
            except ConnectionError as c:
                Tk().withdraw()
                messagebox.showerror("Connection Error", "Internet is not connected"+str(c))
                logInPage()
               
            
            # -----------------------------------------Weather Function---------------------------------------------------#
            def musicPlayer1():
                from MusicPlayer import Music
                frame = Frame(win,width=480, height=720)
                frame.pack(fill=BOTH,expand=True)
                musicFrame = Music()
                musicFrame.musicPlayer(frame, registerwin,name, city)

            # -----------------------------------------Voice Based Assistant Function---------------------------------------------------#
            
            def vbaFun():
                from VBA import VoiceAssitant
                frame = Frame(win,width=480, height=720)
                frame.pack(fill=BOTH,expand=True)
                vbaFrame = VoiceAssitant()
                vbaFrame.voiceAssist(frame, registerwin, name, city)


            # -----------------------------------------Text Based Assistant Function---------------------------------------------------#
            def tbaFun():
                frame = Frame(win,width=480, height=720)
                frame.pack(fill=BOTH,expand=TRUE)
                tbaFrame = TBAClass()
                tbaFrame.tBA(frame, registerwin, name, city)

            # -----------------------------------------Time Function---------------------------------------------------#
            def timenow():
                hr = datetime.now().time().hour
                if hr < 12:
                    return "Good Morning"
                elif 12 < hr < 17:
                    return "Good Afternoon"
                else:
                    return "Good Evening"

            def logInPage():
                frame= Frame(win, width=480,height=720)
                frame.pack(fill="both", expand=True)
                        
                logInFrame = LogIn()
                logInFrame.logIn(frame, registerwin)


            # -------------------------------------------Link's Funtions------------------------------------------------#

            def openLink(link):
                webbrowser.open(link)

            def openCamera():
                os.system("python Camera.py")

            # win = Tk()
            # win.resizable(False,False)
            # win.geometry("480x700")
            win.config(bg="#163A54")
            path = PhotoImage(file="Logo.png")
            head = Label(win, image=path, bg="#163A54")
            head.image = path
            head.place(x=100, y=10)

            # -----------------------------TimeNow Function--------------------#

            def timeNow():
                timeis = datetime.now().strftime("%H : %M : %S")
                timelb.config(text=timeis)
                registerwin.after(1000, timeNow)

            # ---------------------------Jokes----------------------------------#

            def jokes():
                from Jokes import FunnyJokes
                frame = Frame(win, width=480, height=720)
                frame.pack(fill="both", expand=True)
                jokesFrame = FunnyJokes()
                jokesFrame.jokes(frame, registerwin, name, city)

            # ---------------------------Weather Function-----------------------#

            # greeting Image
            greet = Label(win, text="{0}, {1}".format(timenow(), name), bg="#163A54", fg="White",
                          font=("Agency FB", 25))
            greet.place(x=110, y=120)
            cityLb = Label(win, text=city, bg="#163A54", fg="White", font=("Agency FB", 15))
            cityLb.place(x=50, y=230)

            # --------------------------TEMP AFTERNOON--------------------------#
            tempLb = Label(win, text=str(temp) + '°C', bg="#163A54", fg="White", font=("Agency FB", 50))
            tempLb.place(x=150, y=180)

            # --------------------------TEMP EVENING----------------------------#
            greet3 = Label(win, text=data['weather'][0]['main'], bg="#163A54", fg="White", font=("Agency FB", 15))
            greet3.place(x=380, y=230)

            # ---------------------------TRY SOMETHING LIKE THIS----------------#
            tryLb = Label(win, text="Try Something Like This", bg="#163A54", fg="White", font=("Agency FB", 25))
            tryLb.place(x=120, y=300)

            # ---------------------------open youtube------------------------------------#
            youtubeImage = PhotoImage(file="LinkLogo/Youtube.png")
            youtube = Button(win, image=youtubeImage, bg="#163A54", command=lambda: openLink('http://youtube.com'),
                             activebackground='#163A54', bd=0)
            youtube.image = youtubeImage
            youtube.place(x=35, y=400)
            # ---------------------------open facebook---------------------------------------#

            facebookLogo = PhotoImage(file="LinkLogo/Facebook.png")
            facebook = Button(win, image=facebookLogo, bg="#163A54", command=lambda: openLink('http://facebook.com'),
                              activebackground='#163A54', bd=0)
            facebook.image = facebookLogo
            facebook.place(x=265, y=400)

            # --------------------------Open SOG-----------------------------------------#
            sogImage = PhotoImage(file="LinkLogo/SOG.png")
            sog = Button(win, image=sogImage, bg="#163A54", command=lambda: openLink('http://google.com'),
                         activebackground='#163A54', bd=0)
            sog.image = sogImage
            sog.place(x=150, y=460)

            # --------------------------Open Joke-----------------------------------------#
            jokeImage = PhotoImage(file="LinkLogo/Joke.png")
            joke = Button(win, image=jokeImage, bg="#163A54",command=jokes,
                          activebackground='#163A54', bd=0)
            joke.image = jokeImage
            joke.place(x=35, y=520)

            
            # --------------------------Open Weather----------------------------------------#
            weatherImage = PhotoImage(file="LinkLogo/Weather.png")
            weather = Button(win, image=weatherImage, bg="#163A54", command=weatherForcast,
                             activebackground='#163A54', bd=0)
            weather.image = weatherImage
            weather.place(x=265, y=520)
            # --------------------------Open Camera-----------------------------------------#
            cameraImage = PhotoImage(file="LinkLogo/Camera.png")
            camera = Button(win, image=cameraImage, bg="#163A54", command=openCamera,
                     activebackground='#163A54', bd=0)
            camera.image = cameraImage
            camera.place(x=150, y=580)

            # --------------------------Open TBA-----------------------------------WSS------#
            chat = PhotoImage(file="Logo/chat1.png")
            chatbtn = Button(win, image=chat, activebackground="#163A54", bd=0, relief="flat",bg="#163A54", command=tbaFun)
            chatbtn.image=chat
            chatbtn.place(x=50,y=630)

            # --------------------------Open MusicPlayer-----------------------------------WSS------#
            Media = PhotoImage(file="Logo/Media.png")
            Mediabtn = Button(win, image=Media, activebackground="#163A54", bd=0, relief="flat",bg="#163A54", command=musicPlayer1)
            Mediabtn.image=Media
            Mediabtn.place(x=350,y=630)

            # --------------------------Open Voice Based Assistant-----------------------------------WSS------#
            mic = PhotoImage(file="Logo/Mic.png")
            micbtn = Button(win, image=mic, activebackground="#163A54", bd=0, relief="flat",bg="#163A54", command=vbaFun)
            micbtn.image=mic
            micbtn.place(x=200,y=630)


            logOut = Button(win, text="LogOut", font=("Yatra One",10), activebackground="#163A54", bd=0, command=logInPage, bg="#163A54")
            logOut.place(x=0,y=690)

            timelb = Label(win, text="time is here", font=("Orbitron Black", 15), bg='#163A54', fg='white')
            timelb.place(x=340, y=85)
            timeNow()
        except ConnectionError as e:
            messagebox.showerror("Internet Error","Unable to establish Internet Connection")
            messagebox.showerror("Internet Error","Retry After connceting to Internet")