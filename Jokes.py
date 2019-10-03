from tkinter import *
from requests import *
import requests as rqts
from tkinter import scrolledtext
from tkinter import messagebox
import random



class FunnyJokes:
    def jokes(self, jokesWin, window, name, city):
        #jokesWin=Tk()
        #jokesWin.geometry("480x720")
        jokesWin.config(bg="#163A54")
        #jokesWin.resizable(False, False)
        window.title("Jokes")
        logo = PhotoImage(file='Logo.png')
        logoLabel = Label(jokesWin, image=logo, bg="#163A54")
        logoLabel.image=logo
        logoLabel.pack()

        url = "https://gofugly.in/api/content/22"
        global j
        j = 0
        newi = 0
        try:
            data = get(url).json()
        except rqts.exceptions.ConnectionError:
            jokesWin.withdraw()
            messagebox.showerror("Connection Error","Internet is not conncted")
        global jokes
        jokes = []
        
        def mainPage():
            from MainLayoutClass import MainLayout
            frame= Frame(jokesWin, width=480,height=720)
            frame.pack(fill="both", expand=True)
            lab.pack_forget()
            canWin.pack_forget()
            lb.pack_forget()
            lab1.pack_forget()
            logoLabel.pack_forget()

            mainFrame = MainLayout()
            mainFrame.callMain(frame, window, name, city)

        def displayjokes():
            global j, newi, jokes
            try:
                global jokes
                for i in range(j, data['count']):
                    jokes.append(data['result'][i]['joke'])
                    newi = i + 1
            except Exception as E:
                j = newi + 1
                jokesWin.after(1000, displayjokes)
        displayjokes()
        lab = Label(jokesWin, height=10, bg="#163A54")
        lab.pack()
        emoji = PhotoImage(file="Jokes/JOKES1.png")
        emojiLabel = Label(jokesWin, image=emoji, bg="#163A54")
        emojiLabel.place(x=10,y=100)
        jokesLabel = Label(jokesWin, text="JOKES", font=("Orbitron Black", 35), bg="#163A54", fg="White")
        jokesLabel.place(x=130,y=100)
        emojiLabel1 = Label(jokesWin, image=emoji, bg="#163A54")
        emojiLabel1.place(x=350,y=100)
        canWin = scrolledtext.ScrolledText(jokesWin, fg="white", bg="#163A54", font=("Yatra one", 12),width=50, relief=FLAT,
                                            height=13, selectbackground="white", selectforeground="#163A54", selectborderwidth=0)
        canWin.tag_configure("center", justify='center')
        canWin.tag_add("center", 1.0, "end")
        canWin.pack()


        #canWin.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        canWin.delete("1.0", END)
        canWin.insert("1.0", jokes[random.randint(0,135)], "center")

        def getJokes():
            canWin.delete("1.0", END)
            canWin.insert("1.0", jokes[random.randint(0,135)], "center")
            


        lab1 = Label(jokesWin, height=3, bg="#163A54")
        lab1.pack()
        lb=Button(jokesWin, text="Try another one", font=("Orbitron Black", 25), bg="#163A54", fg="White",command=getJokes)
        lb.pack()
        logOut = Button(jokesWin, text="Back", font=("Yatra One",10), activebackground="#163A54", bd=0, command=mainPage, bg="#163A54")
        logOut.place(x=0,y=690)
        jokesWin.mainloop()
