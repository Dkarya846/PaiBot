import os
import random
import datetime
import requests
import webbrowser
from tkinter import *
import wikipedia
#from pygame import mixer
import pyttsx3
import speech_recognition as sr
#from speech_recognition.__main__ import r, audio

paibot = pyttsx3.init()
voices = paibot.getProperty('voices')
paibot.setProperty('voice', voices[0].id)
rate = paibot.getProperty('rate')
paibot.setProperty('rate', rate - 50)

def speak(strs):
    paibot.say(strs)
    paibot.runAndWait()
r=sr.Recognizer()
global input1
input1=""
bgColor = "#163A54"
win = Tk()
win.iconbitmap("PaiBot.ico")
b= 80
win.geometry("480x720")
win.resizable(False, False)
win.config(bg=bgColor)
global botReplyLen, wiki, message
botReplyLen=0

def bot(self):
        try:
                global input1
                with sr.Microphone() as source:
                    print("Tell me something:")
                    audio = r.listen(source)
                    try:
                        input1 = r.recognize_google(audio)
                        print("You said:- " + r.recognize_google(audio))
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        paibot.say('I didnt get that, Could you please repeat it?')
                        paibot.runAndWait()

                sender(input1)
                def get_time():
                        time = datetime.datetime.now().time()
                        receiver("The current Time is: \n"+ str(time))
                def get_date():
                        date = datetime.datetime.now()
                        receiver("The current date is \n"+ str(date))
                greetingsuser = ['hey there', 'hello', 'hi', 'hiiiiiii', 'hey', 'hola', 'namaste', 'sasriyakal']
                greetingsreply = ['Hey There', 'Hello', 'Hi', 'Hiiiiiii', 'Hola, How are you?', 'Hey', 'Hola', 'Namaste', 'Sasriyakal'] 
                question = ['how are you', 'how are you doing?','how are you?','what\'s up?', 'what\'s up',"how are you doing?"]
                responses = ["I'm fine", "I'm cool like the moon", "I'm doing great", "I am raising the Stars ☺"]
                ownerques = ['who made you?', 'who made you', 'who created you', 'who created you?',"who developed you?", "who developed you", "tell me about your developers"]
                ownerans = ['I was created by Pai Programmers ', 'Pai Programmers', 'A group of super Intelligent kidos']
                timevar = ['what time is it', 'what is the time', 'time', "tell me current time", "tell me time"]
                date1 = ['what date is it', 'what is the date', 'date',"tell me current time", "tell me time"]
                aboutme = ['who are you', 'what is your name']
                openbrowser = ['open browser', 'open google']
                media = ['play music', 'play songs', 'play a song', 'open music player']
                jokesquery = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
                jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
                youtube = ['open youtube', 'i want to watch a video']
                goodbyeCommands = ['exit','close','goodbye', 'nothing','bye']
                colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
                favColor = ['what is you favourite colour', 'what is your favourite color','what is your color', 'what is your colour', 'your color', 'your color?']
                humblewords = ['thank you', 'thanks',"i like it"]
                qestOnme = ['Do you Know Me','tell me about me','do you know me','who am i']
                sumit = ['Who is Sumit','who is sumit','who is Sumit','Sumit kaun hi']
                deepak = ['Deepak', 'Who is Deeepak','who is Deepak','who is Deepak','Deepak kaun hai']
                repfr9 = ['You\'re Welcome', 'Glad I Could Help ', "Happy to assist you"]
                abilities = ['what can you do?', 'what can you do', "help me?", "help me", "help", 'what are you abilities', 'what are you abilities?' ]
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
                        elif input1.lower() in media:
                                pass
                        elif input1.lower() in ownerques:
                                reply = random.choice(ownerans)
                                receiver(reply)
                                break
                        elif input1 in cmd9:
                                receiver(random.choice(repfr9))
                                break
                        elif input1 in favColor:
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
                                receiver('I am PaiBot. I am  your Personal Assistant. I am happy to assist you')
                                break
                        elif input1 in youtube:
                                webbrowser.open('www.youtube.com')
                                break
                        elif input1 in goodbyeCommands:
                                print('see you later')
                                exit()
                                break        
                        elif input1 in qestOnme:
                                receiver("You told me you are"+"")
                                break
                        elif input1 in sumit:
                                sumit="Sumit is One of My Intelligent Developer"
                                receiver(sumit)
                                break
                        elif input1 in timevar:
                                get_time()
                                break
                        elif input1 in date1:
                                get_date()
                                break
                        elif input1 in openbrowser:
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
                        elif input1 in deepak:
                                receiver('Deepak is one of My Intelligent creator')
                                break
                        elif "go to" in input1.lower():
                                webbrowser.open(input1[6:])
                                receiver("Done ☻ ")
                                break
                        else:
                                receiver("Sorry, I am afraid I don't know that ☻. I am working hard to know it")
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
        canvas.create_window(5, b, anchor=NW, window=button1)
        b+=button1.winfo_reqheight()+30
def openUrl(self):
        if(str(wiki)==""):
                receiver("No URL Found")
        else:
                webbrowser.open(wiki)

def receiver(botReply):
    global b, message
    message = Message(canvas,text=botReply,width=350, font=("Yatra One",15), bg="white", fg="#163A54")
    canvas.create_window(5,b,window=message,anchor=NW)
    b = b+message.winfo_reqheight()+30
    onFrameConfigure(canvas)
    canvas.yview_moveto(1.0)
    message.bind('<Button-1>', openUrl)
    paibot.say(botReply)
    paibot.runAndWait()

def sender(texts):
    textinput.set("")
    global b
    global message
    message = Message(canvas,text=texts,width=350,font=("Yatra One",15),bg="green", fg="white")
    canvas.create_window(450,b,window=message,anchor=NE)
    b = b+message.winfo_reqheight()+30
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
canvas.pack(side=TOP,expand=True,fill=BOTH)


logo = PhotoImage(file="Logo.png")
canvas.create_image(80, 5, image=logo, anchor=NW)

sendphoto = PhotoImage(file="Logo\Mic.png")
btn2=Button(win, command=lambda:bot("Hello"), image=sendphoto, relief = FLAT, bg=bgColor, activebackground=bgColor)
btn2.place(x=240,y=680)
win.mainloop()
