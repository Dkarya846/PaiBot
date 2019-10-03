from datetime import *
import os
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from pymysql import *
import webbrowser


global city,name
city, name="",""
class LogIn:
    def logIn(self, LogInWin, window):
        window.geometry("480x720")
        window.resizable(False, False)
        window.title("PaiBot LogIn Page")
        LogInWin.config(bg="#163A54")
        window.iconbitmap("PaiBot.ico")


        def registerPage():
            from RegisterPage import Register
            frame= Frame(LogInWin, width=480,height=720)
            frame.pack(fill="both", expand=True)
            window.title("PaiBot Registration Page")
            registerFrame = Register()
            registerFrame.registerPage(frame, window)


        def forgetPage():
            from ForgetPasswordPage import Forget
            frame= Frame(LogInWin, width=480,height=720)
            frame.pack(fill="both", expand=True)
            window.title("PaiBot Password Reset Page")
            forgetFrame = Forget()
            forgetFrame.forgetPage(frame, window)


        def mainPage(self):            
            from MainLayoutClass import MainLayout
            try:
                con = connect(host="localhost", user="root", password="", database="paibot")
                if passWord.get()!="" and email.get()!="":
                    a=con.cursor()
                    a.execute("select * from users where `Email ID`='"+email.get()+"' and Password='"+passWord.get()+"'")            
                    print(a.rowcount)
                    if a.rowcount>0:
                        data = a.fetchall()
                        print(data)
                        name=data[0][0]
                        city = data[0][3]    
                        messagebox.showinfo("Message","LogIn Successful ☻")    
                        frame= Frame(LogInWin, width=480,height=720)
                        frame.pack(fill="both", expand=True)
                        from MainLayoutClass import MainLayout
                        mainFrame = MainLayout()
                        mainFrame.callMain(frame, window, name, city)
                    else:
                        messagebox.showerror("LogIn Error", "Credentials Does not Match")
                else:
                    messagebox.showerror("LogIn Error", "These fields can be left empty")
            except OperationalError as e:
                messagebox.showerror("Database Error","Database Not Connected. Connect it first ☻")

        # ---------------------------Logo-----------------------------#
        img = PhotoImage(file="Logo.png")
        mainlogo = Label(LogInWin, image=img, bg="#163A54")
        mainlogo.place(x=100, y=10)

        logborder = PhotoImage(file="LogIn\\Logborder.png")
        border = Label(LogInWin, image=logborder, bg="#163A54")
        border.place(x=20, y=100)

        logimg = PhotoImage(file="LogIn\\Login.png")
        log = Label(LogInWin, image=logimg, bg="#163A54")
        log.place(x=50, y=88)

        #nameLb = Label(LogInWin, text="Enter Name", font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        #nameLb.place(x=50, y=150)
        #name = Entry(LogInWin, width=31, font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        #name.place(x=50, y=190)


        emailLb = Label(LogInWin, text="Enter Email ID", font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        emailLb.place(x=50, y=200)
        email = Entry(LogInWin, width=31, font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        email.place(x=50, y=240)

        passWordLb = Label(LogInWin, text="Enter PassWord", font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")   
        passWordLb.place(x=50, y=300)
        passWord = Entry(LogInWin, width=31, font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF",show="*")
        passWord.place(x=50, y=340)
        passWord.bind("<Return>",mainPage)

        
        logInLogo = Button(LogInWin, text="LogIn", font=("Yatra One", 20,"bold"), bd=0, bg="#163A54", fg="#FFFFFF", activebackground="#163A54", relief=FLAT, command=lambda:mainPage(1))
        logInLogo.place(x=70, y=450)

        newUserLogo = Button(LogInWin, text="New User?", font=("Yatra One", 20,"bold"), bd=0, bg="#163A54", fg="#FFFFFF", activebackground="#163A54", relief=FLAT, command=registerPage)
        newUserLogo.place(x=250, y=450)
        
        forgotPassLogo =  Button(LogInWin, text="Forgot Password?", font=("Yatra One", 20,"bold"), bd=0, bg="#163A54", fg="#FFFFFF", activebackground="#163A54", relief=FLAT, command=forgetPage)
        forgotPassLogo.place(x=100, y=540)

        
        LogInWin.mainloop()
