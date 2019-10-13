from datetime import *
import os
import time
from tkinter import *
from tkinter import messagebox
from pymysql import *
from PIL import ImageTk, Image
import webbrowser
class Register:
    def registerPage(self, registerWin, window):
        registerWin.config(bg="#163A54")
        window.title("PaiBot Registration Page ☻")
        window.iconbitmap('PaiBot.ico')


        def logIn():
            from LogInPage import LogIn
            window.title("PaiBot LogIn Page ☻")
            frame = Frame(registerWin,width=480, height=720)
            frame.pack(fill=BOTH,expand=TRUE)
            logInFrame = LogIn()
            logInFrame.logIn(frame, window)


        def registerUser():
            print("working")
            try:
                con = connect(host="localhost", user="root", password="", database="paibot")
                a = con.cursor()
                if passWord.get()!="" and name.get()!="" and email.get()!="" and cityIn.get()!="":
                    a.execute("INSERT INTO `users`(`Name`, `Email Id`, `Password`, `City`) VALUES ('"+name.get()+"','"+email.get()+"','"+passWord.get()+"','"+cityIn.get()+"')")
                    con.commit()       
                    messagebox.showinfo("Message","Registration Successful, Log to Continue ☻") 
                    logIn()    
                else:
                    messagebox.showerror("Registration Error", "These fields can be left empty")
            except OperationalError as e:
                messagebox.showerror("Database Error","Database Not Connected. Connect it first ☻")
            except IntegrityError:
                messagebox.showerror("Database Error", "Email Id is already registered")
            except Exception as e:
                messagebox.showerror("Error",str(e))


        

        # ---------------------------Logo-----------------------------#
        img = PhotoImage(file="Logo.png")
        mainlogo = Label(registerWin, image=img, bg="#163A54")
        mainlogo.image = img
        mainlogo.place(x=100, y=10)

        # ---------------------------Border-----------------------------#
        logborder = PhotoImage(file="LogIn/Logborder.png")
        border = Label(registerWin, image=logborder, bg="#163A54")
        border.image=logborder
        border.place(x=20, y=100)

        # ---------------------------RegisterLogo-----------------------------#
        registerimg = PhotoImage(file="Register\\RegisterLogo.png")
        register = Label(registerWin, image=registerimg, bg="#163A54")
        register.image=registerimg
        register.place(x=50, y=88)

        # ---------------------------Name-----------------------------#
        nameLb = Label(registerWin, text="Enter Name", font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        nameLb.place(x=50, y=140)
        name = Entry(registerWin, width=31, font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        name.place(x=50, y=180)

        # ---------------------------Email-----------------------------#
        emailLb = Label(registerWin, text="Enter Your Email", font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        emailLb.place(x=50, y=230)
        email = Entry(registerWin, width=31, font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        email.place(x=50, y=270)

        # ---------------------------Password-----------------------------#
        passWordLb = Label(registerWin, text="Enter PassWord", font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        passWordLb.place(x=50, y=330)
        passWord = Entry(registerWin, width=31, font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF",show="*")
        passWord.place(x=50, y=370)

        # ---------------------------Confirm Password-----------------------------#
        cityLb = Label(registerWin, text="City", font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        cityLb.place(x=50, y=430)
        cityIn = Entry(registerWin, width=31, font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        cityIn.place(x=50, y=470)

        # ---------------------------Registere Button-----------------------------#
        registerLogoimg = PhotoImage(file='LogIn\\Register.png')
        registerLogo = Button(registerWin, image=registerLogoimg, bg="#163A54", activebackground="#163A54", bd=0, command=registerUser)
        registerLogo.image=registerLogoimg
        registerLogo.place(x=40, y=540)

        # ---------------------------Forgot Password-----------------------------#
        #forgotPassLb = Label(registerWin, text="Forgot Password?", font=("Orbitron Black", 15,"bold"), bd=5, bg="#163A54", fg="#FFFFFF")
        #forgotPassLb.place(x=40, y=630)

        # ---------------------------LogIn-----------------------------#
        logInLb = Button(registerWin, text="LogIn Here", font=("Yatra One", 15,"bold"), bd=0, bg="#163A54", fg="#FFFFFF", activebackground="#163A54",
                  relief=FLAT, command=logIn)
        logInLb.place(x=180, y=630)
        registerWin.mainloop()
