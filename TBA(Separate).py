from tkinter import *
import random
import wikipedia
import os
import wikipedia.exceptions
import requests
import datetime
import webbrowser
import time
global b
b=100
bgColor = "#163A54"
win = Tk()
win.title("PaiBot")
win.iconbitmap("PaiBot.ico")
win.geometry("480x720")
win.resizable(False, False)
win.config(bg=bgColor)
global botReplyLen, wiki, message
botReplyLen=0


def bot(self):
        global b
        try:
                input1 = textbox.get()
                sender(input1)
                def get_time():
                        time = datetime.datetime.now().time()
                        receiver("The current Time is: \n"+ str(time))
                def get_date():
                        date = datetime.datetime.now()
                        receiver("The current date is \n"+ str(date))
                greetingsuser = ['hey there', 'hello', 'hi', 'hiiiiiii', 'hey', 'hola', 'namaste', 'sasriyakal']
                greetingsreply = ['Hey There', 'Hello', 'Hi', 'Hiiiiiii', 'Hola, How are you?', 'Hey', 'Hola', 'Namaste', 'Sasriyakal'] 
                question = ['how are you', 'How are you doing?','how Are You','what\'s up?', 'what\'s up?']
                responses = ["I'm fine", "I'm cool like the moon", "I'm doing great", "I am raising the Stars ☺"]
                ownerques = ['who made you?', 'who made you', 'who created you', 'who created you?']
                ownerans = ['I was created by Pai Programmers ', 'Pai Programmers', 'A group of super Intelligent kidos']
                timevar = ['what time is it', 'what is the time', 'time']
                date1 = ['what date is it', 'what is the date', 'date']
                aboutme = ['who are you', 'what is your name']
                cmd1 = ['open browser', 'open google']
                cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
                jokesquery = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
                jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
                cmd4 = ['open youtube', 'i want to watch a video']
                cmd5 = ['tell me the weather', 'weather', 'what about the weather']
                cmd6 = ['exit','close','goodbye', 'nothing','bye']
                cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
                colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
                cmd8 = ['what is you favourite colour', 'what is your favourite color']
                cmd9 = ['thank you']
                cmd10 = ['Do you Know Me','tell me about me','do you know me','who am i']
                cmd11 = ['Who is Sumit','who is sumit','who is Sumit','Sumit kaun hi']
                cmd12 = ['Deepak']
                repfr9 = ['youre welcome', 'glad i could help you']
                
                while True:
                        if input1.lower() in greetingsuser:
                                random_greeting=random.choice(greetingsreply)
                                receiver(random_greeting+", I am PaiBot, How may I assist You?")
                                break
                        elif input1.lower() in question:
                                receiver('I am fine')
                                break
                        elif "calculate" in input1.lower():
                                subs = input1[10:]
                                receiver("Answer is :\n"+str(eval(subs)))
                                break
                        elif input1 in ownerques:
                                reply = random.choice(ownerans)
                                receiver(reply)
                                break
                        elif input1 in cmd9:
                                receiver(random.choice(repfr9))
                                break
                        elif input1 in cmd7:
                                mycolor = random.choice(colrep)+'\nIt keeps changing every micro second'
                                receiver(mycolor)
                                break                
                        elif input1 in cmd8:
                                mycolor = random.choice(colrep)+'\nIt keeps changing every micro second'
                                receiver(mycolor)
                                break
                        elif "temperature" in input1 :
                                temp = input1.split()
                                if len(temp)==5:
                                        url = "http://api.openweathermap.org/data/2.5/weather?q="+temp[4]+"&units=metric&APPID=47657b66139fc2cb733e7566ec239fd1"
                                        data = requests.get(url).json()
                                        receiver("Current Temperature of "+temp[4]+" is "+str(data['main']['temp'])+"°C")
                                elif len(temp)==6:
                                        url = "http://api.openweathermap.org/data/2.5/weather?q="+temp[5]+"&units=metric&APPID=47657b66139fc2cb733e7566ec239fd1"
                                        data = requests.get(url).json()
                                        receiver("Current Temperature of "+temp[5]+" is "+str(data['main']['temp'])+"°C")
                                elif len(temp)==3:
                                        url = "http://api.openweathermap.org/data/2.5/weather?q="+temp[2]+"&units=metric&APPID=47657b66139fc2cb733e7566ec239fd1"
                                        data = requests.get(url).json()
                                        receiver("Current Temperature of "+temp[2]+" is "+str(data['main']['temp'])+"°C")
                                else :
                                        receiver("Data is OFF")
                                
                                break
                        elif input1 in aboutme:
                                receiver('I am  your Personal Assistant')
                                break
                        elif input1 in cmd4:
                                webbrowser.open('www.youtube.com')
                                break
                        elif input1 in cmd6:
                                print('see you later')
                                exit()
                                break        
                        elif input1 in cmd10:
                                print("You Are My Developer,Thanks for Creating Me")
                                break
                        elif input1 in cmd11:
                                sumit="Sumit is boy. He has four leg. His pet name is Chintu. He also has a Tail. He always keep anger on his nose. When he is angry he don't know what he is saying so he needs a tounge cleaner"
                                receiver(sumit)
                                break
                        elif input1 in timevar:
                                get_time()
                                break
                        elif input1 in date1:
                                get_date()
                                break
                        elif input1 in cmd1:
                                receiver('Openning......')
                                webbrowser.open('www.google.com')
                                receiver('Done ☺')
                                break
                        elif input1 in jokesquery:
                                jokre = random.choice(jokes)
                                break
                        elif "about" in input1 :
                                about1 = input1.split()
                                global wiki
                                if len(about1)==4:
                                        strs = str(wikipedia.summary(about1[3]))
                                        wiki = wikipedia.page(about1[3]).url
                                        i = strs.index('.')
                                        receiver(strs[:i+1])
                                        moreAbout(wiki)
                                break
                        elif "open" in input1.lower():
                                os.system(input1.split()[1])
                                break
                        elif input1 in cmd12:
                                receiver('Deepak is one of My Intelligent creator')
                                break
                        elif "go to" in input1.lower():
                                webbrowser.open(input1[6:])
                                receiver("Done ☻ ")
                                break
                        else:
                                receiver("Sorry, I don't know that. But I am still Learning and Improving ☻")
                                break
        except ZeroDivisionError as e:
                receiver(str(e))
        except wikipedia.exceptions.DisambiguationError as e :
                receiver("Too many results")
        except wikipedia.exceptions.PageError as e:
                receiver("No details found kindly check Spellings in input")
        except requests.exceptions.ConnectionError as e:        
                receiver("Internet is not connected")

def moreAbout(url):
        global b
        button1 = Button(win, text = "Click Here For More", command = lambda:openUrl(url), anchor = W, bg="white")
        button1.configure(width = 20, height=2, activebackground = "white", relief = FLAT, justify=CENTER, font=("Yatra One",15))
        canvas.create_window(5, b, anchor=NW, win=button1)
        b+=button1.winfo_reqheight()+30
def openUrl(self):
        if(str(wiki)==""):
                receiver("No URL Found")
        else:
                webbrowser.open(wiki)

def receiver(botReply):
        global b, message
        message = Message(canvas,text=botReply,width=350, font=("Yatra One",15), bg="white", fg="#163A54")
        canvas.create_window(50,b,win=message,anchor=NW)
                
        b = b+message.winfo_reqheight()+10
        onFrameConfigure(canvas)
        canvas.yview_moveto(1.0)
        message.bind('<Button-1>', openUrl)


def sender(texts):
        textinput.set("")
        global b
        global message
        message = Message(canvas,text=texts,width=350,font=("Yatra One",15),bg="green", fg="white")
        canvas.create_window(512,b,win=message,anchor=NE)
        b = b+message.winfo_reqheight()+10
        onFrameConfigure(canvas)
        canvas.yview_moveto(1.0)

frame=Frame(win,width=460,height=720,bg=bgColor)
frame.place(x=0,y=0)

canvas=Canvas(frame,bg=bgColor, width=480,height=680, bd=0, relief='ridge', highlightthickness=0)
vbar=Scrollbar(canvas,orient=VERTICAL,elementborderwidth=-3)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(yscrollcommand=vbar.set)

def onFrameConfigure(canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))
win.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
canvas.pack(side=LEFT,expand=True,fill=BOTH)

textinput=StringVar()
textbox=Entry(win, width=27,font=("Yatra One", 19), bg=bgColor, fg="#FFFFFF", textvariable=textinput)
textbox.place(x=40,y=680)
textbox.bind('<Return>',bot)

#logo = PhotoImage(file="Logo.png")
#canvas.create_image(80, 5, image=logo)



sendphoto = PhotoImage(file="sendButton.png")
btn2=Button(win, command=lambda:bot("Hello"), image=sendphoto, relief = FLAT, bg=bgColor, activebackground=bgColor, bd=0)
btn2.place(x=450,y=685)

back=PhotoImage(file="Logo/back.png")
backbtn = Button(win, text="Back", image=back, font=("Yatra One",10), relief = FLAT, activebackground="#163A54", bd=0, bg="#163A54")
backbtn.image=back
backbtn.place(x=0,y=680)

win.mainloop()