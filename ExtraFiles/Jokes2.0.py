from tkinter import *
from requests import *
import requests as rqts
from tkinter import scrolledtext
from tkinter import messagebox


jokesWin=Tk()
jokesWin.geometry("480x720")
jokesWin.config(bg="#163A54")
jokesWin.resizable(False, False)
jokesWin.title("Jokes")
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
def displayjokes():
    global j, newi, jokes
    try:
        global jokes
        for i in range(j, data['count']):
            jokes.append(data['result'][i]['joke'])
            newi = i + 1
    except Exception as E:
        print("Jokes is Not Available right now")
        j = newi + 1
        jokesWin.after(1000, displayjokes)
displayjokes()
lab = Label(jokesWin, height=25, bg="#163A54")
lab.pack()
canvas=Canvas(jokesWin,bg="#163A54", width=480,height=680, bd=0, relief='ridge', highlightthickness=0)
vbar=Scrollbar(canvas,orient=VERTICAL,elementborderwidth=-3)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(yscrollcommand=vbar.set)


def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))
jokesWin.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
canvas.pack(side=TOP,expand=True,fill=BOTH)

textinput=StringVar()
lb=Label(jokesWin, text="Try another one", font=("Orbitron Black", 25))
lb.pack()
jokesWin.mainloop()
