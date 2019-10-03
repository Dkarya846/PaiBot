import requests
from tkinter import *
import urllib
from tkinter import messagebox
import time

global data
data=""
class Weather:
    def getWeather(self, weatherWin, window, name, city1):
        try:    
            def mainPage():
                from MainLayoutClass import MainLayout
                frame= Frame(weatherWin, width=480,height=720)
                frame.pack(fill="both", expand=True)
                mainFrame = MainLayout()
                mainFrame.callMain(frame, window, name, city1)
    
            def getForcasting(self):
                try:    
                    city=inputCityText.get()
                    url = "http://api.openweathermap.org/data/2.5/forecast?q="+city+"&units=metric&APPID=47657b66139fc2cb733e7566ec239fd1"
                    global data    
                    data = requests.get(url).json()
                    

                    
                    temp = Label(weatherWin, text=str(data['list'][0]["main"]["temp"])+"°C\t", font=("Orbitron Black",20), bg=bgColor, fg="#FFFFFF")
                    temp.place(x=180, y=330)

                    humidity = Label(weatherWin, text=str(data['list'][0]["main"]["humidity"])+"\t", font=("Orbitron Black",20), bg=bgColor, fg="#FFFFFF")
                    humidity.place(x=80, y=360)
                    
                    humiditylb = Label(weatherWin, text="Humidity", font=("Orbitron Black",20), bg=bgColor, fg="#FFFFFF")
                    humiditylb.place(x=35, y=400)

                    weatherIcon = "http://openweathermap.org/img/w/"+str(data['list'][0]["weather"][0]["icon"])+".png"
                    urllib.request.urlretrieve(weatherIcon, "weatherType.png")
                    weathertype=PhotoImage(file="weatherType.png")
                    typelb = Label(weatherWin, image=weathertype, bg=bgColor) 
                    typelb.image=weathertype
                    typelb.place(x=350,y=360)

                    typelb2 = Label(weatherWin, text=str(data['list'][0]['weather'][0]["main"])+"\t", font=("Orbitron Black",20), bg=bgColor, fg="#FFFFFF")
                    typelb2.place(x=330, y=400)

                    
                    y1=460
                    day = Label(weatherWin, text="Day", font = ("Yatra One",12), justify=CENTER, width=12, bg="black", fg="white")
                    day.place(x=10,y=y1)
                    temp = Label(weatherWin, text="Temperature", font = ("Yatra One",12), justify=CENTER, width=12, bg="black", fg="white")
                    temp.place(x=140,y=y1)
                    type = Label(weatherWin, text="Type", font = ("Yatra One",12), justify=CENTER, width=8, bg="black", fg="white")
                    type.place(x=270,y=y1)
                    wind = Label(weatherWin, text="Wind(KM/S)", font = ("Yatra One",12), justify=CENTER, width=10, bg="black", fg="white")
                    wind.place(x=360,y=y1)

                    day1Color="#FF7F50"
                    day1 = Label(weatherWin, text="Today", font = ("Yatra One",12), justify=CENTER, width=12, bg=day1Color, fg="#FFFFFF")
                    day1.place(x=10,y=y1+40)
                    temp1 = Label(weatherWin, text=str(data['list'][0]["main"]["temp"])+"°C", font = ("Yatra One",12), justify=CENTER, width=12, bg=day1Color, fg="#FFFFFF")
                    temp1.place(x=140,y=y1+40)
                    type1 = Label(weatherWin, text=str(data['list'][0]["weather"][0]["main"]), font = ("Yatra One",12), justify=CENTER, width=8, bg=day1Color, fg="#FFFFFF")
                    type1.place(x=270,y=y1+40)
                    wind1 = Label(weatherWin, text=str(data['list'][0]["wind"]['speed'])+" KM/S", font = ("Yatra One",12), justify=CENTER, width=10, bg=day1Color, fg="#FFFFFF")
                    wind1.place(x=360,y=y1+40)

                    day2Color = "#008000"
                    day2 = Label(weatherWin, text=str(data['list'][3]['dt_txt'])[:10], font = ("Yatra One",12), justify=CENTER, width=12, bg=day2Color, fg="#FFFFFF")
                    day2.place(x=10,y=y1+80)
                    temp2 = Label(weatherWin, text=str(data['list'][3]["main"]["temp"])+"°C", font = ("Yatra One",12), justify=CENTER, width=12, bg=day2Color, fg="#FFFFFF")
                    temp2.place(x=140,y=y1+80)
                    type2 = Label(weatherWin, text=str(data['list'][3]["weather"][0]["main"]), font = ("Yatra One",12), justify=CENTER, width=8, bg=day2Color, fg="#FFFFFF")
                    type2.place(x=270,y=y1+80)
                    wind2 = Label(weatherWin, text=str(data['list'][0]["wind"]['speed'])+" KM/S", font = ("Yatra One",12), justify=CENTER, width=10, bg=day2Color, fg="#FFFFFF")
                    wind2.place(x=360,y=y1+80)

                    day3Color = "#008B8B"
                    day3 = Label(weatherWin, text=str(data['list'][11]['dt_txt'])[:10], font = ("Yatra One",12), justify=CENTER, width=12, fg="white", bg=day3Color)
                    day3.place(x=10,y=y1+120)
                    temp3 = Label(weatherWin, text=str(data['list'][11]["main"]["temp"])+"°C", font = ("Yatra One",12), justify=CENTER, width=12, fg="white", bg=day3Color)
                    temp3.place(x=140,y=y1+120)
                    type3 = Label(weatherWin, text=str(data['list'][11]["weather"][0]["main"]), font = ("Yatra One",12), justify=CENTER, width=8, fg="white", bg=day3Color)
                    type3.place(x=270,y=y1+120)
                    wind3 = Label(weatherWin, text=str(data['list'][11]["wind"]['speed'])+" KM/S", font = ("Yatra One",12), justify=CENTER, width=10, fg="white", bg=day3Color)
                    wind3.place(x=360,y=y1+120)

                    day4Color="#9068be"
                    day4 = Label(weatherWin, text=str(data['list'][19]['dt_txt'])[:10], font = ("Yatra One",12), justify=CENTER, width=12, fg="white", bg=day4Color)
                    day4.place(x=10,y=y1+160)
                    temp4 = Label(weatherWin, text=str(data['list'][19]["main"]["temp"])+"°C", font = ("Yatra One",12), justify=CENTER, width=12, fg="white", bg=day4Color)
                    temp4.place(x=140,y=y1+160)
                    type4 = Label(weatherWin, text=str(data['list'][19]["weather"][0]["main"]), font = ("Yatra One",12), justify=CENTER, width=8, fg="white", bg=day4Color)
                    type4.place(x=270,y=y1+160)
                    wind4 = Label(weatherWin, text=str(data['list'][19]["wind"]['speed'])+" KM/S", font = ("Yatra One",12), justify=CENTER, width=10, fg="white", bg=day4Color)
                    wind4.place(x=360,y=y1+160)

                    day5Color="#7d4627"
                    day5 = Label(weatherWin, text=str(data['list'][27]['dt_txt'])[:10], font = ("Yatra One",12), justify=CENTER, width=12, fg="white", bg=day5Color)
                    day5.place(x=10,y=y1+200)
                    temp5 = Label(weatherWin, text=str(data['list'][27]["main"]["temp"])+"°C", font = ("Yatra One",12), justify=CENTER, width=12, fg="white", bg=day5Color)
                    temp5.place(x=140,y=y1+200)
                    type5 = Label(weatherWin, text=str(data['list'][27]["weather"][0]["main"]), font = ("Yatra One",12), justify=CENTER, width=8, fg="white", bg=day5Color)
                    type5.place(x=270,y=y1+200)
                    wind5 = Label(weatherWin, text=str(data['list'][27]["wind"]['speed'])+" KM/S", font = ("Yatra One",12), justify=CENTER, width=10, fg="white", bg=day5Color)
                    wind5.place(x=360,y=y1+200)
                except KeyError as e:
                    messagebox.askretrycancel("Error", "City Not Found")
                except Exception as e:
                    messagebox.askretrycancel("Error", str(e))
        
            bgColor = "#163A54"
            weatherWin.config(bg=bgColor)

            window.title("PaiBot Weather Report")
            logo = PhotoImage(file='Logo.png')
            logoLabel = Label(weatherWin, image=logo, bg=bgColor)
            logoLabel.image=logo
            logoLabel.place(x=100,y=10)
            
            searchboximg = PhotoImage(file="searchbutton.png")
            searchLabel = Label(weatherWin, image=searchboximg, bg=bgColor)
            searchLabel.image=searchboximg
            searchLabel.place(x=0,y=130)

            inputCityText = Entry(weatherWin, font=("Yatra One",18),width=25, bd=5, fg="#AC213E", bg="#1FA5AD", relief=FLAT, justify=CENTER)
            inputCityText.place(x=38,y=142)
            inputCityText.bind("<Return>",getForcasting)

            srchimg = PhotoImage(file="Searchicon.png")
            srchButton = Button(weatherWin, image=srchimg, bg=bgColor, relief=FLAT
                        , activebackground=bgColor, command=lambda:getForcasting(0), bd=0)
            srchButton.image=srchimg
            srchButton.place(x=200,y=220)
            logOut = Button(weatherWin, text="Back", font=("Yatra One",10), activebackground="#163A54", bd=0, command=mainPage, bg="#163A54")
            logOut.place(x=0,y=690)

        except KeyError:
            print("City not found")
        weatherWin.mainloop()