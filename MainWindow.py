from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from WindowSettings import Window
from ManagementSystem import ManagementSystem
import sqlite3


def main():
    MWn = Window(root)
    app = MainWindow(MWn.win(450, 466, 0, 0))
    root.mainloop()


class MainWindow(Window, ManagementSystem):
    def __init__(self, master):
        self.master = master
        self.d = Database()
        self.d.conn()

        self.master.title("LOGIN SYSTEM")

        self.MainFrame = Frame(self.master, bg="lavender", bd=5, relief=RIDGE)
        self.MainFrame.pack(fill=BOTH)

        self.Img1 = ImageTk.PhotoImage(Image.open("Images/login.png"))
        self.ImgLabel = Label(self.MainFrame, image=self.Img1, bd=0)
        self.ImgLabel.pack(padx=0, pady=30)

        self.LoginFrame = Frame(self.MainFrame, bd=0, bg="lavender")
        self.LoginFrame.pack(side=TOP)

        self.UserLabel = Label(self.LoginFrame, text="USER: ", bg="lavender", font=("Garamond", 15, "bold"), fg="black")
        self.UserLabel.grid(row=0, column=0, padx=20, pady=10, sticky=E)

        self.PassLabel = Label(self.LoginFrame, text="PASSWORD: ", bg="lavender", font=("Garamond", 15, "bold"),
                               fg="black")
        self.PassLabel.grid(row=1, column=0, padx=20, pady=0, sticky=E)

        self.UserTxt = Entry(self.LoginFrame, width=21, bg="azure3", font=("Garamond", 15, "bold"), fg="black")
        self.UserTxt.bind("<KeyRelease>", self.check_user)
        self.UserTxt.bind("<Escape>", self.quit)
        self.UserTxt.bind("<Return>", self.enter)
        self.UserTxt.grid(row=0, column=1, padx=5, pady=0)
        self.UserTxt.focus()

        self.PassTxt = Entry(self.LoginFrame, width=21, bg="azure3", font=("Garamond", 15, "bold"), fg="black", show="*")
        self.PassTxt.bind("<KeyRelease>", self.check_pass)
        self.PassTxt.bind("<Escape>", self.quit)
        self.PassTxt.bind("<Return>", self.enter)
        self.PassTxt.grid(row=1, column=1, padx=5, pady=30)

        self.MsgLabel = Label(self.LoginFrame, text="Don't have an account?", bg="lavender",
                              font=("Garamond", 12, "bold"), fg="black")
        self.MsgLabel.grid(row=2, column=0, padx=5, sticky=E)

        self.LineLabel = Label(self.LoginFrame, text="REGISTER HERE.", bg="lavender", font=("Garamond", 10, "bold")
                               , fg="darkolivegreen")
        self.LineLabel.place(width=110, height=20, x=35, y=155)

        self.Img2 = ImageTk.PhotoImage(Image.open("Images/register.png"))
        self.RegisterBtn = Button(self.LoginFrame, image=self.Img2, bd=2, command=self.register)
        self.RegisterBtn.grid(row=3, column=0, pady=20, sticky=N)

        self.SignLabel = Label(self.LoginFrame, text="         Sign in.", bg="lavender",
                               font=("Garamond", 12, "bold"), fg="black")
        self.SignLabel.grid(row=2, column=1, sticky=N)

        self.Line1Label = Label(self.LoginFrame, text="CLICK HERE.", bg="lavender", font=("Garamond", 10, "bold")
                                , fg="darkolivegreen")
        self.Line1Label.place(width=100, height=20, x=247, y=155)

        self.Img3 = ImageTk.PhotoImage(Image.open("Images/sign.png"))
        self.SignBtn = Button(self.LoginFrame, image=self.Img3, bd=2, command=lambda: self.enter(""), state=DISABLED)
        self.SignBtn.grid(row=3, column=1, padx=50, pady=20, sticky=E)

    def check_user(self, event):
        Msg1Label = Label(self.MainFrame, text="Invalid username", bg="lavender",
                          font=("Garamond", 10, "bold"), fg="maroon")
        Msg2Label = Label(self.MainFrame, text="Username found", bg="lavender",
                          font=("Garamond", 10, "bold"), fg="yellowgreen")
        Msg3Label = Label(self.MainFrame, text="", bg="lavender",
                          font=("Garamond", 10, "bold"), fg="lavender")
        user = self.d.check_user(self.UserTxt.get())
        cl1 = []

        self.SignBtn.config(state=DISABLED)

        if self.UserTxt.get() == "":
            Msg3Label.place(width=100, height=20, x=255, y=178)
            self.UserTxt.config(bg="azure3")
        elif user == cl1:
            Msg1Label.place(width=100, height=20, x=257, y=178)
            self.UserTxt.config(bg="mistyrose")
        elif user[0][0] == self.UserTxt.get():
            Msg2Label.place(width=100, height=20, x=257, y=178)
            self.UserTxt.config(bg="yellowgreen")
            if user[0][0] == self.UserTxt.get() and user[0][1] == self.PassTxt.get():
                self.SignBtn.config(state=NORMAL)

    def check_pass(self, event):
        Msg1Label = Label(self.MainFrame, text="Invalid password", bg="lavender",
                          font=("Garamond", 10, "bold"), fg="maroon")
        Msg2Label = Label(self.MainFrame, text="Correct password", bg="lavender",
                          font=("Garamond", 10, "bold"), fg="yellowgreen")
        Msg3Label = Label(self.MainFrame, text="", bg="lavender",
                          font=("Garamond", 10, "bold"), fg="lavender")
        Msg4Label = Label(self.MainFrame, text="Please check username", bg="lavender",
                          font=("Garamond", 10, "bold"), fg="maroon")
        user = self.d.check_user(self.UserTxt.get())
        cl1 = []

        self.SignBtn.config(state=DISABLED)

        if self.PassTxt.get() == "":
            Msg3Label.place(width=150, height=20, x=233, y=245)
            self.PassTxt.config(bg="azure3")
        elif user == cl1:
            Msg4Label.place(width=150, height=20, x=233, y=245)
            self.PassTxt.config(bg="mistyrose")
        elif user[0][1] != self.PassTxt.get():
            Msg1Label.place(width=100, height=20, x=257, y=245)
            self.PassTxt.config(bg="mistyrose")
        elif user[0][1] == self.PassTxt.get():
            Msg2Label.place(width=100, height=20, x=257, y=245)
            self.PassTxt.config(bg="yellowgreen")
            if user[0][1] == self.PassTxt.get() and user[0][0] == self.UserTxt.get():
                self.SignBtn.config(state=NORMAL)

    def enter(self, event):
        user = self.d.check_user(self.UserTxt.get())
        cl1 = []
        if user == cl1:
            cl = messagebox.showerror("LOGIN", "INVALID DATA, USER NOT FOUND.")
            if cl == "ok":
                self.UserTxt.delete(0, END)
                self.UserTxt.focus()
        elif user[0][1] == self.PassTxt.get():
            top = Toplevel(self.master)
            InWin = Window(top)
            app = ManagementSystem(InWin.win(1000, 600, 0, 30))
            top.focus()
            self.master.withdraw()
        else:
            cl = messagebox.showerror("LOGIN", "INVALID PASSWORD, TRY AGAIN.")
            if cl == "ok":
                self.PassTxt.delete(0, END)
                self.PassTxt.focus()

    def register(self):
        top = Toplevel(self.master)
        RegWin = Window(top)
        app = Register(RegWin.win(500, 648, 0, 30))
        top.focus()
        root.withdraw()

    def quit(self, event):
        self.master.destroy()


class Register:
    def __init__(self, master):
        self.master = master
        self.master.title("REGISTER")

        d = Database()
        d.conn()

        self.MainFrame = Frame(self.master, bg="lavender", bd=5, relief=RIDGE)
        self.MainFrame.pack(fill=BOTH)

        self.Img1 = ImageTk.PhotoImage(Image.open("Images/register1.png"))
        self.ImgLabel = Label(self.MainFrame, image=self.Img1, bd=0)
        self.ImgLabel.pack(padx=0, pady=30)

        self.RegisterFrame = Frame(self.MainFrame, bd=0, bg="lavender")
        self.RegisterFrame.pack(side=TOP)

        self.TypeLabel = Label(self.RegisterFrame, text="DOCUMENT TYPE: ", bg="lavender", font=("Garamond", 15, "bold"),
                               fg="black")
        self.TypeLabel.grid(row=0, column=0, padx=20, pady=10, sticky=E)

        self.TypesLabel = Label(self.RegisterFrame, bg="lavender")
        self.TypesLabel.grid(row=0, column=1, pady=10, sticky=W)

        Types = [
            ("ID", 1),
            ("PASSPORT", 2)
        ]

        Type = IntVar()
        Type.set(1)
        Doc = StringVar()
        User = StringVar()
        Email = StringVar()
        Pass = StringVar()
        Pass2 = StringVar()

        for Texts, T in Types:
            Radiobutton(self.TypesLabel, bg="lavender", font=("Garamond", 10), fg="black",
                        text=Texts, variable=Type, value=T, command=lambda: clicked(Type.get())).pack(anchor=W)

        def clicked(value):
            Msg1Label = Label(self.MainFrame, text="Document already registered", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")
            Msg2Label = Label(self.MainFrame, text="Valid document", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="yellowgreen")
            Msg3Label = Label(self.MainFrame, text="", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="lavender")
            Type.set(value)

            cl = d.select_users(Doc.get())
            cl1 = []

            if Type.get() == 1 and len(Doc.get()) > 0:
                Msg4Label = Label(self.MainFrame, text="Document must be 10 numbers", bg="lavender",
                                  font=("Garamond", 10, "bold"), fg="maroon")
                if Doc.get() == "":
                    Msg3Label.place(width=180, height=20, x=280, y=250)
                    self.DocTxt.config(bg="azure3")
                elif len(Doc.get()) != 10:
                    Msg4Label.place(width=180, height=20, x=280, y=250)
                    self.DocTxt.config(bg="cornsilk")
                    self.RegisterBtn.config(state=DISABLED)
                elif len(Doc.get()) == 10:
                    if cl == cl1:
                        Msg2Label.place(width=180, height=20, x=280, y=250)
                        self.DocTxt.config(bg="yellowgreen")
                        if check is not False and User.get() != "" and Email.get() != "" and Pass.get() != "" \
                                and Pass2.get() != "":
                            self.RegisterBtn.config(state=NORMAL)
                    elif cl[0][0] == int(Doc.get()):
                        Msg1Label.place(width=180, height=20, x=275, y=250)
                        self.DocTxt.config(bg="mistyrose")
            elif Type.get() == 2 and len(Doc.get()) > 0:
                Msg4Label = Label(self.MainFrame, text="Document must be 5 numbers", bg="lavender",
                                  font=("Garamond", 10, "bold"), fg="maroon")
                if Doc.get() == "":
                    Msg3Label.place(width=180, height=20, x=280, y=250)
                    self.DocTxt.config(bg="azure3")
                elif len(Doc.get()) != 5:
                    Msg4Label.place(width=180, height=20, x=280, y=250)
                    self.DocTxt.config(bg="cornsilk")
                    self.RegisterBtn.config(state=DISABLED)
                elif len(Doc.get()) == 5:
                    if cl == cl1:
                        Msg2Label.place(width=180, height=20, x=280, y=250)
                        self.DocTxt.config(bg="yellowgreen")
                        if check is not False and User.get() != "" and Email.get() != "" and Pass.get() != "" \
                                and Pass2.get() != "":
                            self.RegisterBtn.config(state=NORMAL)
                    elif cl[0][0] == int(Doc.get()):
                        Msg1Label.place(width=180, height=20, x=278, y=250)
                        self.DocTxt.config(bg="mistyrose")

        def check():
            Em = Email.get()
            if len(User.get()) < 6:
                cl = messagebox.showwarning("REGISTER", "Username length has to be greater than 5.")
                if cl == "ok":
                    self.master.focus()
                    self.UserTxt.focus()
                    return False
            if Em[-10:] != "@gmail.com" and Em[-12:] != "@hotmail.com":
                cl = messagebox.showwarning("REGISTER", "Invalid email. Must be either gmail or hotmail.")
                if cl == "ok":
                    self.master.focus()
                    self.EmailTxt.focus()
                    return False
            if Type.get() == 1:
                if len(Doc.get()) != 10 and Pass.get() != Pass2.get():
                    cl = messagebox.showwarning("REGISTER", "Identification document has to be 10 characters long and\n"
                                                            "passwords have to be equal. Try again.")
                    if cl == "ok":
                        self.master.focus()
                        self.DocTxt.focus()
                    return False
                if len(Doc.get()) != 10:
                    cl = messagebox.showwarning("REGISTER", "Identification document has to be 10 characters long.")
                    if cl == "ok":
                        self.master.focus()
                        self.DocTxt.focus()
                    return False
            if Type.get() == 2:
                if len(Doc.get()) != 5 and Pass.get() != Pass2.get():
                    cl = messagebox.showwarning("REGISTER", "Passport has to be 5 characters long and passwords have\n"
                                                            "to be equal.")
                    if cl == "ok":
                        self.master.focus()
                        self.DocTxt.focus()
                        return False
                if len(Doc.get()) != 5:
                    cl = messagebox.showwarning("REGISTER", "Passport has to be 5 characters long.")
                    if cl == "ok":
                        self.master.focus()
                        self.DocTxt.focus()
                        return False
            if Pass.get() != Pass2.get():
                cl = messagebox.showwarning("REGISTER", "Passwords are not equal. Try again.")
                if cl == "ok":
                    Pass.set("")
                    Pass2.set("")
                    self.master.focus()
                    self.PassTxt.focus()
                    return False
            if len(Pass.get()) < 4:
                cl = messagebox.showwarning("REGISTER", "Passwords lengths have to be greater than 3. Try again.")
                if cl == "ok":
                    Pass.set("")
                    Pass2.set("")
                    self.master.focus()
                    self.PassTxt.focus()
                    return False

        def insert(event):
            if check() is False:
                print("CHECK INSERTED DATA.")
            else:
                cl = messagebox.askquestion("REGISTER", "Do you want to add " + User.get() + "?")
                if cl == "yes":
                    d.insert_user(Doc.get(), Type.get(), User.get(), Email.get(), Pass.get())
                    Doc.set("")
                    Type.set(1)
                    User.set("")
                    Email.set("")
                    Pass.set("")
                    Pass2.set("")
                    self.DocTxt.config(bg="azure3")
                    self.UserTxt.config(bg="azure3")
                    self.EmailTxt.config(bg="azure3")
                    self.PassTxt.config(bg="azure3")
                    self.Pass2Txt.config(bg="azure3")
                    Msg1Label = Label(self.MainFrame, text="", bg="lavender",
                                      font=("Garamond", 10, "bold"), fg="lavender")
                    Msg1Label.place(width=180, height=20, x=280, y=250)
                    Msg2Label = Label(self.MainFrame, text="", bg="lavender",
                                      font=("Garamond", 10, "bold"), fg="lavender")
                    Msg2Label.place(width=180, height=20, x=280, y=298)
                    Msg3Label = Label(self.MainFrame, text="", bg="lavender",
                                      font=("Garamond", 10, "bold"), fg="lavender")
                    Msg3Label.place(width=180, height=20, x=280, y=346)
                    Msg4Label = Label(self.MainFrame, text="", bg="lavender",
                                      font=("Garamond", 10, "bold"), fg="lavender")
                    Msg4Label.place(width=180, height=20, x=280, y=394)
                    Msg5Label = Label(self.MainFrame, text="", bg="lavender",
                                      font=("Garamond", 10, "bold"), fg="lavender")
                    Msg5Label.place(width=180, height=20, x=280, y=442)
                    self.DocTxt.focus()
                else:
                    self.master.focus()

        def checkDoc(event):
            Msg1Label = Label(self.MainFrame, text="Document already registered", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")
            Msg2Label = Label(self.MainFrame, text="Valid document", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="yellowgreen")
            Msg3Label = Label(self.MainFrame, text="", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="lavender")
            Msg4Label = Label(self.MainFrame, text="Document must be 10 numbers", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")

            cl = d.select_users(Doc.get())
            cl1 = []

            self.RegisterBtn.config(state=DISABLED)

            if Type.get() == 1:
                if Doc.get() == "":
                    Msg3Label.place(width=180, height=20, x=280, y=250)
                    self.DocTxt.config(bg="azure3")
                elif len(Doc.get()) != 10:
                    Msg4Label.place(width=180, height=20, x=280, y=250)
                    self.DocTxt.config(bg="cornsilk")
                elif len(Doc.get()) == 10:
                    if cl == cl1:
                        Msg2Label.place(width=180, height=20, x=280, y=250)
                        self.DocTxt.config(bg="yellowgreen")
                        if check is not False and User.get() != "" and Email.get() != "" and Pass.get() != "" \
                                and Pass2.get() != "":
                            self.RegisterBtn.config(state=NORMAL)
                    elif cl[0][0] == int(Doc.get()):
                        Msg1Label.place(width=180, height=20, x=275, y=250)
                        self.DocTxt.config(bg="mistyrose")

            elif Type.get() == 2:
                Msg4Label = Label(self.MainFrame, text="Document must be 5 numbers", bg="lavender",
                                  font=("Garamond", 10, "bold"), fg="maroon")
                if Doc.get() == "":
                    Msg3Label.place(width=180, height=20, x=280, y=250)
                    self.DocTxt.config(bg="azure3")
                elif len(Doc.get()) != 5:
                    Msg4Label.place(width=180, height=20, x=280, y=250)
                    self.DocTxt.config(bg="cornsilk")
                elif len(Doc.get()) == 5:
                    if cl == cl1:
                        Msg2Label.place(width=180, height=20, x=280, y=250)
                        self.DocTxt.config(bg="yellowgreen")
                        if check is not False and User.get() != "" and Email.get() != "" and Pass.get() != "" \
                                and Pass2.get() != "":
                            self.RegisterBtn.config(state=NORMAL)
                    elif cl[0][0] == int(Doc.get()):
                        Msg1Label.place(width=180, height=20, x=278, y=250)
                        self.DocTxt.config(bg="mistyrose")

        def checkUser(event):
            Msg1Label = Label(self.MainFrame, text="User already registered", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")
            Msg2Label = Label(self.MainFrame, text="User available", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="yellowgreen")
            Msg3Label = Label(self.MainFrame, text="", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="lavender")
            Msg4Label = Label(self.MainFrame, text="Insufficient length", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")

            cl = d.select_users("", User.get())
            cl1 = []

            self.RegisterBtn.config(state=DISABLED)

            if User.get() == "":
                Msg3Label.place(width=180, height=20, x=280, y=298)
                self.UserTxt.config(bg="azure3")
                self.RegisterBtn.config(state=DISABLED)
            elif len(User.get()) < 6:
                Msg4Label.place(width=180, height=20, x=280, y=298)
                self.UserTxt.config(bg="cornsilk")
                self.RegisterBtn.config(state=DISABLED)
            else:
                if cl == cl1:
                    Msg2Label.place(width=180, height=20, x=280, y=298)
                    self.UserTxt.config(bg="yellowgreen")
                    if check is not False and Doc.get() != "" and Email.get() != "" and Pass.get() != "" \
                            and Pass2.get() != "":
                        self.RegisterBtn.config(state=NORMAL)
                elif cl[0][1] == User.get():
                    Msg1Label.place(width=180, height=20, x=275, y=298)
                    self.UserTxt.config(bg="mistyrose")
                    self.RegisterBtn.config(state=DISABLED)

        def checkEmail(event):
            Msg1Label = Label(self.MainFrame, text="Email already registered", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")
            Msg2Label = Label(self.MainFrame, text="Email available", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="yellowgreen")
            Msg3Label = Label(self.MainFrame, text="", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="lavender")
            Msg4Label = Label(self.MainFrame, text="Invalid email", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")

            cl = d.select_users("", "", Email.get())
            cl1 = []
            Em = Email.get()

            self.RegisterBtn.config(state=DISABLED)

            if Email.get() == "":
                Msg3Label.place(width=180, height=20, x=280, y=346)
                self.EmailTxt.config(bg="azure3")
            elif len(Email.get()) < 6 or Em[-10:] != "@gmail.com" and Em[-12:] != "@hotmail.com":
                Msg4Label.place(width=180, height=20, x=280, y=346)
                self.EmailTxt.config(bg="cornsilk")
            else:
                if cl == cl1:
                    Msg2Label.place(width=180, height=20, x=280, y=346)
                    self.EmailTxt.config(bg="yellowgreen")
                    if check is not False and Doc.get() != "" and User.get() != "" and Pass.get() != "" \
                            and Pass2.get() != "":
                        self.RegisterBtn.config(state=NORMAL)
                elif cl[0][2] == Email.get():
                    Msg1Label.place(width=180, height=20, x=278, y=346)
                    self.EmailTxt.config(bg="mistyrose")

        def checkPass(event):
            Msg1Label = Label(self.MainFrame, text="Correct", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="yellowgreen")
            Msg2Label = Label(self.MainFrame, text="Insufficient length", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")
            Msg3Label = Label(self.MainFrame, text="", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="lavender")
            Msg4Label = Label(self.MainFrame, text="Passwords coincide", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="yellowgreen")
            Msg5Label = Label(self.MainFrame, text="Passwords don't coincide", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")
            Msg6Label = Label(self.MainFrame, text="Passwords coincide", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="yellowgreen")
            Msg7Label = Label(self.MainFrame, text="Passwords don't coincide", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")

            self.RegisterBtn.config(state=DISABLED)

            if Pass.get() == "":
                Msg3Label.place(width=180, height=20, x=280, y=394)
                self.PassTxt.config(bg="azure3")
                if len(Pass2.get()) > 3:
                    Msg7Label.place(width=180, height=20, x=278, y=442)
                    self.Pass2Txt.config(bg="mistyrose")
            elif len(Pass.get()) < 4:
                Msg2Label.place(width=180, height=20, x=278, y=394)
                self.PassTxt.config(bg="cornsilk")
            elif Pass2.get() != "" and len(Pass2.get()) > 3:
                if Pass.get() == Pass2.get():
                    Msg4Label.place(width=180, height=20, x=278, y=394)
                    Msg6Label.place(width=180, height=20, x=280, y=442)
                    self.PassTxt.config(bg="yellowgreen")
                    self.Pass2Txt.config(bg="yellowgreen")
                    if check is not False and User.get() != "" and Email.get() != "" and Doc.get() != "" \
                            and Pass2.get() != "":
                        self.RegisterBtn.config(state=NORMAL)
                else:
                    Msg5Label.place(width=180, height=20, x=278, y=394)
                    Msg3Label.place(width=180, height=20, x=280, y=442)
                    Msg2Label.place(width=180, height=20, x=280, y=442)
                    self.PassTxt.config(bg="mistyrose")
                    self.Pass2Txt.config(bg="mistyrose")
            else:
                Msg1Label.place(width=180, height=20, x=278, y=394)
                self.PassTxt.config(bg="yellowgreen")
                if check is not False and User.get() != "" and Email.get() != "" and Doc.get() != "" \
                        and Pass2.get() != "":
                    self.RegisterBtn.config(state=NORMAL)

        def checkPass2(event):
            Msg1Label = Label(self.MainFrame, text="Passwords coincide", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="yellowgreen")
            Msg2Label = Label(self.MainFrame, text="Insufficient length", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")
            Msg3Label = Label(self.MainFrame, text="", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="lavender")
            Msg4Label = Label(self.MainFrame, text="Passwords don't coincide", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")
            Msg6Label = Label(self.MainFrame, text="Passwords coincide", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="yellowgreen")
            Msg7Label = Label(self.MainFrame, text="Passwords don't coincide", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="maroon")
            Msg8Label = Label(self.MainFrame, text="Correct", bg="lavender",
                              font=("Garamond", 10, "bold"), fg="yellowgreen")

            self.RegisterBtn.config(state=DISABLED)

            if Pass2.get() == "":
                Msg3Label.place(width=180, height=20, x=280, y=442)
                self.Pass2Txt.config(bg="azure3")
                if len(Pass.get()) > 3:
                    Msg8Label.place(width=180, height=20, x=278, y=394)
                    self.PassTxt.config(bg="yellowgreen")
                else:
                    Msg2Label.place(width=180, height=20, x=278, y=394)
                    self.PassTxt.config(bg="cornsilk")
            elif Pass.get() != "":
                if Pass.get() == Pass2.get() and len(Pass.get()) > 3:
                    Msg3Label.place(width=180, height=20, x=278, y=394)
                    Msg1Label.place(width=180, height=20, x=280, y=442)
                    Msg6Label.place(width=180, height=20, x=280, y=394)
                    self.PassTxt.config(bg="yellowgreen")
                    self.Pass2Txt.config(bg="yellowgreen")
                    if check is not False and User.get() != "" and Email.get() != "" and Doc.get() != "" \
                            and Pass.get() != "":
                        self.RegisterBtn.config(state=NORMAL)
                else:
                    Msg3Label.place(width=180, height=20, x=278, y=394)
                    Msg2Label.place(width=180, height=20, x=280, y=442)
                    Msg7Label.place(width=180, height=20, x=280, y=394)
                    self.PassTxt.config(bg="mistyrose")
                    self.Pass2Txt.config(bg="mistyrose")
            if Pass2.get() != "":
                if len(Pass2.get()) < 4:
                    Msg2Label.place(width=180, height=20, x=278, y=442)
                    self.Pass2Txt.config(bg="cornsilk")
                elif Pass.get() == Pass2.get():
                    Msg1Label.place(width=180, height=20, x=278, y=442)
                    self.Pass2Txt.config(bg="yellowgreen")
                    if check is not False and User.get() != "" and Email.get() != "" and Doc.get() != "" \
                            and Pass.get() != "":
                        self.RegisterBtn.config(state=NORMAL)
                else:
                    Msg4Label.place(width=180, height=20, x=278, y=442)
                    self.Pass2Txt.config(bg="mistyrose")

        def back(event):
            self.master.destroy()
            root.deiconify()

        self.DocLabel = Label(self.RegisterFrame, text="DOCUMENT: ", bg="lavender", font=("Garamond", 15, "bold"),
                              fg="black")
        self.DocLabel.grid(row=1, column=0, padx=20, pady=10, sticky=E)

        self.DocTxt = Entry(self.RegisterFrame, width=21, bg="azure3", font=("Garamond", 15, "bold"), fg="black",
                            textvariable=Doc)
        self.DocTxt.bind("<KeyRelease>", checkDoc)
        self.DocTxt.bind("<Return>", insert)
        self.DocTxt.bind("<Escape>", back)
        self.DocTxt.bind("<Alt-Left>", back)
        self.DocTxt.grid(row=1, column=1)

        self.DocTxt.focus()

        self.UserLabel = Label(self.RegisterFrame, text="USER: ", bg="lavender", font=("Garamond", 15, "bold"),
                               fg="black")
        self.UserLabel.grid(row=2, column=0, padx=20, pady=10, sticky=E)

        self.UserTxt = Entry(self.RegisterFrame, width=21, bg="azure3", font=("Garamond", 15, "bold"), fg="black",
                             textvariable=User)
        self.UserTxt.bind("<KeyRelease>", checkUser)
        self.UserTxt.bind("<Return>", insert)
        self.UserTxt.bind("<Escape>", back)
        self.UserTxt.bind("<Alt-Left>", back)
        self.UserTxt.grid(row=2, column=1)

        self.EmailLabel = Label(self.RegisterFrame, text="EMAIL: : ", bg="lavender", font=("Garamond", 15, "bold"),
                                fg="black")
        self.EmailLabel.grid(row=3, column=0, padx=20, pady=10, sticky=E)

        self.EmailTxt = Entry(self.RegisterFrame, width=21, bg="azure3", font=("Garamond", 15, "bold"), fg="black",
                              textvariable=Email)
        self.EmailTxt.bind("<KeyRelease>", checkEmail)
        self.EmailTxt.bind("<Return>", insert)
        self.EmailTxt.bind("<Escape>", back)
        self.EmailTxt.bind("<Alt-Left>", back)
        self.EmailTxt.grid(row=3, column=1)

        self.PassLabel = Label(self.RegisterFrame, text="PASSWORD: ", bg="lavender", font=("Garamond", 15, "bold"),
                               fg="black")
        self.PassLabel.grid(row=4, column=0, padx=20, pady=10, sticky=E)

        self.PassTxt = Entry(self.RegisterFrame, width=21, bg="azure3", font=("Garamond", 15, "bold"), fg="black",
                             show="*", textvariable=Pass)
        self.PassTxt.bind("<KeyRelease>", checkPass)
        self.PassTxt.bind("<Return>", insert)
        self.PassTxt.bind("<Escape>", back)
        self.PassTxt.bind("<Alt-Left>", back)
        self.PassTxt.grid(row=4, column=1)

        self.Pass2Label = Label(self.RegisterFrame, text="REPEAT PASSWORD: ", bg="lavender",
                                font=("Garamond", 15, "bold"), fg="black")
        self.Pass2Label.grid(row=5, column=0, padx=20, pady=10, sticky=E)

        self.Pass2Txt = Entry(self.RegisterFrame, width=21, bg="azure3", font=("Garamond", 15, "bold"), fg="black",
                              show="*", textvariable=Pass2)
        self.Pass2Txt.bind("<KeyRelease>", checkPass2)
        self.Pass2Txt.bind("<Return>", insert)
        self.Pass2Txt.bind("<Escape>", back)
        self.Pass2Txt.bind("<Alt-Left>", back)
        self.Pass2Txt.grid(row=5, column=1)

        self.MsgLabel = Label(self.RegisterFrame, text="Register", bg="lavender",
                              font=("Garamond", 12, "bold"), fg="black")
        self.MsgLabel.grid(row=6, column=0, padx=5, pady=10, sticky=N)

        self.Img2 = ImageTk.PhotoImage(Image.open("Images/register2.png"))
        self.RegisterBtn = Button(self.RegisterFrame, image=self.Img2, bd=2, command=lambda: insert(""), state=DISABLED)
        self.RegisterBtn.grid(row=7, column=0, pady=20, sticky=N)

        self.SignLabel = Label(self.RegisterFrame, text="         Go back", bg="lavender",
                               font=("Garamond", 12, "bold"), fg="black")
        self.SignLabel.grid(row=6, column=1, pady=10, sticky=N)

        self.Img3 = ImageTk.PhotoImage(Image.open("Images/home.png"))
        self.BackBtn = Button(self.RegisterFrame, image=self.Img3, bd=2, command=lambda: back(""))
        self.BackBtn.grid(row=7, column=1, padx=50, pady=20, sticky=E)


class Database:
    @staticmethod
    def conn():
        conn = sqlite3.connect("Database/login.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists type (
                    id_type integer primary key,
                    type text
                )""")
        c.execute("""CREATE TABLE if not exists users (
                    document integer primary key,
                    id_type integer,
                    username text,
                    email text,
                    password text
                )""")
        conn.commit()
        conn.close()
        print("DATABASE CONNECTED.")

    @staticmethod
    def insert_types(i, t):
        conn = sqlite3.connect("Database/login.db")
        c = conn.cursor()
        query = "INSERT INTO type VALUES (?, ?)"
        c.execute(query, (i, t))
        conn.commit()
        conn.close()
        print("TYPE " + str(i) + " CREATED")

    @staticmethod
    def insert_user(doc, i, user, email, password):
        conn = sqlite3.connect("Database/login.db")
        c = conn.cursor()
        query = "INSERT INTO users VALUES (?, ?, ?, ?, ?)"
        c.execute(query, (doc, i, user, email, password))
        conn.commit()
        conn.close()
        print("USER " + str(doc) + " INSERTED.")

    @staticmethod
    def check_user(user):
        conn = sqlite3.connect("Database/login.db")
        c = conn.cursor()
        query = "SELECT username, password FROM users WHERE username=?"
        c.execute(query, (user, ))
        row = c.fetchall()
        conn.commit()
        conn.close()
        return row

    @staticmethod
    def select_users(doc="", username="", email=""):
        conn = sqlite3.connect("Database/login.db")
        c = conn.cursor()
        query = "SELECT document, username, email FROM users WHERE document=? or username=? or email=?"
        c.execute(query, (doc, username, email))
        row = c.fetchall()
        conn.commit()
        conn.close()
        return row


if __name__ == '__main__':
    root = Tk()
    main()
