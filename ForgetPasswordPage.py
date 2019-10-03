from datetime import *
import os
import time
from tkinter import *
from tkinter import messagebox
from pymysql import *
from PIL import ImageTk, Image
import webbrowser


class Forget:
    def forgetPage(self, forgetWin, window):
        
        forgetWin.config(bg="#163A54")
        window.title("Password Reset Page ☻")
        window.iconbitmap('PaiBot.ico')

        def registerPage():
            from RegisterPage import Register
            frame= Frame(forgetWin, width=480,height=720)
            frame.pack(fill="both", expand=True)
            window.title("PaiBot Registration Page")
            registerFrame = Register()
            registerFrame.registerPage(frame, window)


        def logIn():
            from LogInPage import LogIn
            frame = Frame(forgetWin,width=480, height=720)
            window.title("PaiBot LogIn Page ☻")
            frame.pack(fill=BOTH,expand=TRUE)
            logInFrame = LogIn()
            logInFrame.logIn(frame, window)


        def forgetUser():
            try:
                con = connect(host="localhost", user="root", password="", database="paibot")
                a = con.cursor()
                if newPass.get()!="" and name.get()!="" and email.get()!="" and conPass.get()!="":
                    a.execute("select * from users where `Email Id`='"+email.get()+"' and Name='"+name.get()+"'")
                    data = a.fetchall()
                    if a.rowcount>0:
                        if conPass.get()==newPass.get():
                            a.execute("update users set Password='"+newPass.get()+"' where `Email Id`='"+email.get()+"'")
                            con.commit()  
                            messagebox.showinfo("Update Information","Password reset Successful")
                            logIn()
                        else:
                            messagebox.showerror("Password Error", "New Password and Confirm Password are not same")
                    else:
                        messagebox.showerror("Error","Please enter a valid User Name and Email Address")
                else:
                    messagebox.showerror("Registration Error", "These fields can be left empty")
            except OperationalError as e:
                messagebox.showerror("Database Error","Database Not Connected. Connect it first ☻")
            except Exception as e:
                messagebox.showerror("Exception Caught",str(e))

        


        # ---------------------------Logo-----------------------------#
        img = PhotoImage(file="Logo.png")
        mainlogo = Label(forgetWin, image=img, bg="#163A54")
        mainlogo.image = img
        mainlogo.place(x=100, y=10)

        # ---------------------------Border-----------------------------#
        logborder = PhotoImage(file="LogIn/Logborder.png")
        border = Label(forgetWin, image=logborder, bg="#163A54")
        border.image=logborder
        border.place(x=20, y=100)

        # ---------------------------ForgetLogo-----------------------------#
        #registerimg = PhotoImage(file="Register\\RegisterLogo.png")
        forget = Label(forgetWin, text="Forget Page", font=("Yatra One", 20,"bold"), bd=0, bg="#163A54", fg="#FFFFFF",
                  relief=FLAT)
        #register.image=registerimg
        forget.place(x=50, y=83)

        # ---------------------------Name-----------------------------#
        nameLb = Label(forgetWin, text="Enter Name", font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        nameLb.place(x=50, y=140)
        name = Entry(forgetWin, width=31, font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        name.place(x=50, y=180)

        # ---------------------------Email-----------------------------#
        emailLb = Label(forgetWin, text="Enter Your Email", font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        emailLb.place(x=50, y=230)
        email = Entry(forgetWin, width=31, font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        email.place(x=50, y=270)

        # ---------------------------Password-----------------------------#
        newPassLb = Label(forgetWin, text="Enter New PassWord", font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        newPassLb.place(x=50, y=330)
        newPass = Entry(forgetWin, width=31, font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF",show="*")
        newPass.place(x=50, y=370)

        # ---------------------------Confirm Password-----------------------------#
        conPassLb = Label(forgetWin, text="Confirm Password", font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF")
        conPassLb.place(x=50, y=430)
        conPass = Entry(forgetWin, width=31, font=("Yatra One", 15), bd=5, bg="#163A54", fg="#FFFFFF", show="*")
        conPass.place(x=50, y=470)

        # ---------------------------Forget Password Button-----------------------------#

        forgetLogo = Button(forgetWin, text="Save", font=("Yatra One", 20,"bold"), bd=0, bg="#163A54", fg="#FFFFFF", activebackground="#163A54",
                  relief=FLAT, command=forgetUser)
        forgetLogo.place(x=70, y=540)

        # ---------------------------Forgot Password-----------------------------#
        #forgotPassLb = Label(forgetWin, text="Forgot Password?", font=("Orbitron Black", 15,"bold"), bd=5, bg="#163A54", fg="#FFFFFF")
        #forgotPassLb.place(x=40, y=630)

        # ---------------------------LogIn-----------------------------#
        logInLb = Button(forgetWin, text="LogIn Here", font=("Yatra One", 20,"bold"), bd=0, bg="#163A54", fg="#FFFFFF", activebackground="#163A54",
                  relief=FLAT, command=logIn)
        logInLb.place(x=250, y=540)

        registerLb = Button(forgetWin, text="Register Here", font=("Yatra One", 20,"bold"), bd=0, bg="#163A54", fg="#FFFFFF", activebackground="#163A54",
                  relief=FLAT, command=registerPage)
        registerLb.place(x=130, y=610)
        forgetWin.mainloop()