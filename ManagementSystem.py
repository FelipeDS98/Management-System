from tkinter import *
from tkinter import font as f
from tkinter import ttk
from tkcalendar import *
from Database import Database
from datetime import date, datetime
from tkinter import messagebox
import random


class ManagementSystem(Database):
    def __init__(self, master):
        self.master = master
        self.master.title("MANAGEMENT SYSTEM")
        self.master.focus()

        d = Database()
        d.conn()

        Font1 = f.Font(family="Garamond", size=12, weight=f.BOLD)
        Font2 = f.Font(family="Garamond", size=12)
        Font3 = f.Font(family="Garamond", size=11)

        Color1 = StringVar()
        Color2 = StringVar()
        Color3 = StringVar()
        Color1.set("azure3")
        Color2.set("azure2")
        Color3.set("azure")

        global d1
        Today = date.today()
        d1 = Today.strftime("%d/%m/%Y")

        def insert_client():
            cl = messagebox.askyesno("CLIENT", "Do you want to insert " + self.NameTxt.get() + "?")
            if cl == 1:
                d.insert_client(self.IDCTxt.get(), self.NameTxt.get(), self.AddressTxt.get(), Gender.get(),
                                Cal.get_date().strftime("%d/%m/%Y"), self.PhoneTxt.get(), self.EmailTxt.get())
                show_clients()
                update()

        def insert_product():
            cl = messagebox.askyesno("PRODUCT", "Do you want to insert " + self.ProductNameTxt.get() + "?")
            if cl == 1:
                k = 0
                for j in range(len(a)):
                    if a[j] == Select.get():
                        k = j + 1
                d.insert_product(self.IDPTxt.get(), self.ProductNameTxt.get(), self.PriceTxt.get(), k,
                                 self.StockTxt.get(), self.CompanyTxt.get(), self.PPhoneTxt.get())
                show_products()
                update()

        def clear_show_clients():
            self.IDCTxt.delete(0, END)
            self.NameTxt.delete(0, END)
            self.AddressTxt.delete(0, END)
            Gender.set(1)
            Cal.set_date(d1)
            self.PhoneTxt.delete(0, END)
            self.EmailTxt.delete(0, END)
            show_clients()
            update()

        def show_clients():
            self.ClientList.delete(0, END)
            for row in d.show_clients():
                self.ClientList.insert(END, row)
            update()

        def clear_show_products():
            self.IDPTxt.delete(0, END)
            self.ProductNameTxt.delete(0, END)
            self.PriceTxt.delete(0, END)
            Select.set(options[0])
            self.StockTxt.delete(0, END)
            self.CompanyTxt.delete(0, END)
            self.PPhoneTxt.delete(0, END)
            show_products()
            update()

        def show_products():
            self.ProductList.delete(0, END)
            for row in d.show_products():
                self.ProductList.insert(END, row)

        def clients_rec(event):
            try:
                global cd

                searchCd = self.ClientList.curselection()[0]
                cd = self.ClientList.get(searchCd)

                cl = d.select_client(cd[4])

                print(getting_age(cl[0][4]))

                self.IDCTxt.delete(0, END)
                self.IDCTxt.insert(END, cl[0][0])

                self.NameTxt.delete(0, END)
                self.NameTxt.insert(END, cl[0][1])

                self.AddressTxt.delete(0, END)
                self.AddressTxt.insert(END, cl[0][2])

                Gender.set(cl[0][3])

                Cal.set_date(cl[0][4])

                self.PhoneTxt.delete(0, END)
                self.PhoneTxt.insert(END, cl[0][5])

                self.EmailTxt.delete(0, END)
                self.EmailTxt.insert(END, cl[0][6])

                update()

            except IndexError as err:
                print("Selection error:", err)

        def delete_client():
            cl = messagebox.askyesno("CLIENT", "Do you want to delete " + self.NameTxt.get() + "?")
            if len(self.IDCTxt.get()) != 0:
                if cl > 0:
                    d.delete_client(cd[4])
                    clear_show_clients()
                    update()

        def update_client():
            cl = messagebox.askyesno("CLIENT", "Do you want to update " + self.NameTxt.get() + "?")
            if cl > 0:
                d.delete_client(cd[4])
                d.insert_client(self.IDCTxt.get(), self.NameTxt.get(), self.AddressTxt.get(), Gender.get(),
                                Cal.get_date().strftime("%d/%m/%Y"), self.PhoneTxt.get(), self.EmailTxt.get())
                clear_show_clients()
                update()

        def search_client():
            self.ClientList.delete(0, END)
            for row in d.search_client(self.IDCTxt.get(), self.NameTxt.get(), self.AddressTxt.get(),
                                       self.PhoneTxt.get(), self.EmailTxt.get()):
                self.ClientList.insert(END, *row)
                update()

        def products_rec(event):
            try:
                global pd

                searchPd = self.ProductList.curselection()[0]
                pd = self.ProductList.get(searchPd)

                cl = d.select_product(pd[4])

                self.IDPTxt.delete(0, END)
                self.IDPTxt.insert(END, cl[0][0])

                self.ProductNameTxt.delete(0, END)
                self.ProductNameTxt.insert(END, cl[0][1])

                self.PriceTxt.delete(0, END)
                self.PriceTxt.insert(END, cl[0][2])

                Select.set(options[cl[0][3] - 1])

                self.StockTxt.delete(0, END)
                self.StockTxt.insert(END, cl[0][4])

                self.CompanyTxt.delete(0, END)
                self.CompanyTxt.insert(END, cl[0][5])

                self.PPhoneTxt.delete(0, END)
                self.PPhoneTxt.insert(END, cl[0][6])

                update()

            except IndexError as err:
                print("Selection error:", err)

        def delete_product():
            cl = messagebox.askyesno("PRODUCT", "Do you want to delete " + self.ProductNameTxt.get() + "?")
            if len(self.IDPTxt.get()) != 0:
                if cl > 0:
                    d.delete_product(pd[4])
                    clear_show_products()
                    update()

        def update_product():
            cl = messagebox.askyesno("PRODUCT", "Do you want to update " + self.ProductNameTxt.get() + "?")
            if cl > 0:
                d.delete_product(pd[4])
                k = 0
                for j in range(len(a)):
                    if a[j] == Select.get():
                        k = j + 1
                d.insert_product(self.IDPTxt.get(), self.ProductNameTxt.get(), self.PriceTxt.get(), k,
                                 self.StockTxt.get(), self.CompanyTxt.get(), self.PPhoneTxt.get())
                clear_show_products()
                update()

        def search_product():
            self.ProductList.delete(0, END)
            for row in d.search_product(self.IDPTxt.get(), self.ProductNameTxt.get(), self.CompanyTxt.get()):
                self.ProductList.insert(END, *row)
                update()
        
        def getting_age(d3):
            dp = date(int(d3[-4:]), int(d3[-7:-5]), int(d3[-10: -8]))
            Now = date.today()
            dn = Now.strftime("%d%m%Y")
            d2 = dp.strftime("%d%m%Y")
            print(dn, d2)
            if int(dn[-6:-4]) > int(d2[-6:-4]) or (int(dn[-6:-4]) == int(d2[-6:-4]) and int(dn[-8:-6]) >= int(d2[-8:-6])):
                return int(dn[-4:]) - int(d2[-4:])
            else:
                return int(dn[-4:]) - int(d2[-4:]) - 1

        Gender = IntVar()
        Gender.set(1)

        types = d.show_type()
        a = []

        for i in range(len(types)):
            a.append(types[i][1])

        options = a

        Select = StringVar()
        Select.set(options[0])

        def clicked(value):
            Gender.set(value)

        def update():
            global c
            global values
            global l1
            global r

            self.SelectUser["value"] = ()
            values = list(self.SelectUser["value"])
            values.append("")

            c = []
            l1 = d.display_clients()

            for r in range(len(l1)):
                c.append(l1[r][0])

            self.SelectUser["value"] = values + c
            self.SelectUser.current(0)
            self.SelectUser.bind("<<ComboboxSelected>>", c_select)
            self.SelectUser.place(width=100, height=23, x=8, y=61)

            self.SelectProduct["value"] = ()
            values = list(self.SelectProduct["value"])
            values.append("")

            c = []
            l1 = d.display_products()

            for r in range(len(l1)):
                c.append(l1[r][1])

            self.SelectProduct["value"] = values + c
            self.SelectProduct.current(0)
            self.SelectProduct.bind("<<ComboboxSelected>>", p_select)
            self.SelectProduct.place(width=100, height=23, x=111, y=61)

        def c_select(event):
            global client_id
            client_id = UserSelected.get()
            cli = d.display_clients()
            for j in range(len(cli)):
                if cli[j][0] == client_id:
                    client_id = cli[j][1]
            print("Client ID:", client_id)

        def p_select(event):
            try:
                global stock
                global product_id
                stock = IntVar()
                product_id = ProductSelected.get()
                pr = d.display_products()
                for j in range(len(pr)):
                    if pr[j][1] == product_id:
                        product_id = pr[j][0]
                s = d.select_ps(product_id)
                stock.set(s[0][1])
                self.QuantitySelect.config(state=NORMAL)
                self.ButtonRight.config(state=NORMAL)
                print("Product ID:", product_id)
                print("Price:", s[0][0])
                print("Stock:", stock.get())
            except IndexError:
                cl = messagebox.showwarning("PRODUCT SELECT", "Please select an item.")
                self.QuantitySelect.config(state=DISABLED)
                self.ButtonLeft.config(state=DISABLED)
                self.ButtonRight.config(state=DISABLED)

        def insert_purchase():
            cl = messagebox.askyesno("TRANSACTION", "Do you want to insert " + self.ProductNameTxt.get() + "?")
            if cl == 1:
                x = random.randint(10908, 500876)
                d.insert_purchase(x, client_id, product_id, quantity.get())
                clear_show_transactions()

        def clear_show_transactions():
            self.SelectUser.current(0)
            self.SelectProduct.current(0)
            quantity.set(0)
            self.QuantitySelect.config(state=DISABLED)
            self.ButtonLeft.config(state=DISABLED)
            self.ButtonRight.config(state=DISABLED)
            show_transactions()

        def show_transactions():
            self.TrList.delete(0, END)
            for row in d.show_transactions():
                self.TrList.insert(END, row)

        def tr_rec(event):
            try:
                global tr

                searchPd = self.TrList.curselection()[0]
                tr = self.TrList.get(searchPd)

                cl = d.select_purchase(tr[0])
                cl1 = d.get_price(cl[0][2])

                self.IDTrTxt.config(state=NORMAL)
                self.IDTrTxt.delete(0, END)
                self.IDTrTxt.insert(END, cl[0][0])
                self.IDTrTxt.config(state=DISABLED)

                self.IDCliTxt.config(state=NORMAL)
                self.IDCliTxt.delete(0, END)
                self.IDCliTxt.insert(END, cl[0][1])
                self.IDCliTxt.config(state=DISABLED)

                self.IDProTxt.config(state=NORMAL)
                self.IDProTxt.delete(0, END)
                self.IDProTxt.insert(END, cl[0][2])
                self.IDProTxt.config(state=DISABLED)

                self.QuaTxt.config(state=NORMAL)
                self.QuaTxt.delete(0, END)
                self.QuaTxt.insert(END, cl[0][3])
                self.QuaTxt.config(state=DISABLED)

                self.TotalTxt.config(state=NORMAL)
                self.TotalTxt.delete(0, END)
                self.TotalTxt.insert(END, str(int(cl[0][3]) * int(cl1[0][0])) + " USD")
                self.TotalTxt.config(state=DISABLED)

                self.TotalPesosTxt.config(state=NORMAL)
                self.TotalPesosTxt.delete(0, END)
                self.TotalPesosTxt.insert(END, str((int(cl[0][3]) * int(cl1[0][0]))*float(3768.50)) + " COP")
                self.TotalPesosTxt.config(state=DISABLED)
                self.BillButton.config(state=NORMAL)

            except IndexError as err:
                print("Selection error:", err)

        def billing():
            now = datetime.now()
            hr = now.strftime("%H:%M:%S")

            self.Billing.config(state=NORMAL)
            self.Billing.delete("1.0", END)
            cl = d.get_price(self.IDProTxt.get())
            cl1 = d.select_client(self.IDCliTxt.get())
            ind = cl1[0][1].index("_")
            gd = d.get_gender(cl1[0][3])
            age = getting_age(cl1[0][4])
            self.Billing.insert(END, "\t\t                SANTANA S.A.\n")
            self.Billing.insert(END, "\t\t           Musical Instruments.\n\n")
            self.Billing.insert(END, "   DATE: " + d1 + ".\t\t\t\t   C.C: " + str(cl1[0][0]) + ".\n")
            self.Billing.insert(END, "   TIME: " + hr + ".\t\t\t\t   NAME: " + cl1[0][1][:ind] + ".\n")
            self.Billing.insert(END, "   COMPANY: " + cl[0][1] + ".\t\t\t\t   SURNAME: " + cl1[0][1][ind+1:] + ".\n")
            self.Billing.insert(END, "   PRODUCT: " + cl[0][2] + ".\t\t\t\t   GENDER: " + gd[0][0] + ".\n")
            self.Billing.insert(END, "   PRICE: " + cl[0][0] + "  -  QTY: " + self.QuaTxt.get() + "\t\t\t\t   AGE: "
                                +  str(age) + ".\n")
            self.Billing.insert(END, "   TOTAL: " + self.TotalTxt.get() + ".\t\t\t\t   PHONE: " + cl1[0][5] +
                                ".\n")
            self.Billing.config(state=DISABLED)

        self.MainFrame = Frame(self.master, bd=5, relief=RIDGE)
        self.MainFrame.pack(fill=BOTH)

        self.LeftFrame = Frame(self.MainFrame, width=500, height=600, bg="lavender", relief=RIDGE)
        self.LeftFrame.pack(side=LEFT, fill=BOTH)

        self.RightFrame = Frame(self.MainFrame, width=500,  height=600, bg="lavender", relief=RIDGE)
        self.RightFrame.pack(side=RIGHT)

        self.ClientsFrame = Frame(self.LeftFrame, bg=Color1.get(), bd=2, relief=RIDGE)
        self.ClientsFrame.pack(side=TOP, padx=5, pady=(5, 0), fill=BOTH)

        self.Msg = Label(self.ClientsFrame, text="Clients Management", bg=Color1.get(), font=Font1)
        self.Msg.place(width=150, height=20, x=10, y=5)

        self.Label = Label(self.ClientsFrame, text="\n", bg=Color1.get(), font=Font2, bd=0)
        self.Label.grid(row=0, column=0, sticky=W)

        self.IDCLabel = Label(self.ClientsFrame, text="ID:", bg=Color1.get(), font=Font2)
        self.IDCLabel.grid(row=1, column=0, sticky=E)

        self.IDCTxt = Entry(self.ClientsFrame, bg=Color2.get(), font=Font1)
        self.IDCTxt.place(width=148, height=23, x=111, y=37)
        self.IDCTxt.focus()

        self.NameLabel = Label(self.ClientsFrame, text="Name:", bg=Color1.get(), font=Font2)
        self.NameLabel.grid(row=2, column=0, sticky=E)

        self.NameTxt = Entry(self.ClientsFrame, bg=Color2.get(), font=Font1)
        self.NameTxt.place(width=148, height=23, x=111, y=61)

        self.AddressLabel = Label(self.ClientsFrame, text="Address:", bg=Color1.get(), font=Font2)
        self.AddressLabel.grid(row=3, column=0, sticky=E)

        self.AddressTxt = Entry(self.ClientsFrame, bg=Color2.get(), font=Font1)
        self.AddressTxt.place(width=148, height=23, x=111, y=85)

        self.Gender = Label(self.ClientsFrame, bg=Color1.get())
        self.Gender.grid(row=4, column=1, ipadx=40, padx=(0, 220))

        Radiobutton(self.Gender, bg=Color1.get(), font=("Garamond", 10, "bold"), text="M", variable=Gender, value=1,
                    command=lambda: clicked(Gender.get())).pack(side=LEFT, anchor=W)

        Radiobutton(self.Gender, bg=Color1.get(), font=("Garamond", 10, "bold"), text="F", variable=Gender, value=2,
                    command=lambda: clicked(Gender.get())).pack(anchor=W)

        self.GenderLabel = Label(self.ClientsFrame, text="Gender:", bg=Color1.get(), font=Font2)
        self.GenderLabel.grid(row=4, column=0, sticky=E)

        self.BirthLabel = Label(self.ClientsFrame, text="Date of Birth:", bg=Color1.get(), font=Font2)
        self.BirthLabel.grid(row=5, column=0, sticky=E)

        Cal = DateEntry(self.ClientsFrame, font=Font1, borderwidth=2, bordercolor="ivory",
                        headersbackground="beige", selectbackground="darkolivegreen", weekendbackground="wheat",
                        weekendforeground="black", date_pattern="dd/mm/yyyy", width=13)
        Cal.grid(row=5, column=1, padx=(0, 244), pady=(0, 2))
        Cal.set_date(d1)

        self.PhoneLabel = Label(self.ClientsFrame, text="Phone Number:", bg=Color1.get(), font=Font2)
        self.PhoneLabel.grid(row=6, column=0, sticky=E)

        self.PhoneTxt = Entry(self.ClientsFrame, bg=Color2.get(), font=Font1, width=18)
        self.PhoneTxt.place(width=148, height=23, x=111, y=163)

        self.EmailLabel = Label(self.ClientsFrame, text="Email Address:", bg=Color1.get(), font=Font2)
        self.EmailLabel.grid(row=7, column=0, sticky=E, pady=(0, 70))

        self.EmailTxt = Entry(self.ClientsFrame, bg=Color2.get(), font=Font1)
        self.EmailTxt.place(width=148, height=23, x=111, y=187)

        self.ClearBtn = Button(self.ClientsFrame, text="CLEAR", bg=Color3.get(), font=Font1, width=6,
                               command=clear_show_clients)
        self.ClearBtn.place(width=80, height=32, x=10, y=230)

        self.SaveBtn = Button(self.ClientsFrame, text="SAVE", bg=Color3.get(), font=Font1, width=6,
                              command=insert_client)
        self.SaveBtn.place(width=80, height=32, x=105, y=230)

        self.UpdateBtn = Button(self.ClientsFrame, text="UPDATE", bg=Color3.get(), font=Font1, width=6,
                                command=update_client)
        self.UpdateBtn.place(width=80, height=32, x=200, y=230)

        self.SearchBtn = Button(self.ClientsFrame, text="SEARCH", bg=Color3.get(), font=Font1, width=6,
                                command=search_client)
        self.SearchBtn.place(width=80, height=32, x=295, y=230)

        self.DeleteBtn = Button(self.ClientsFrame, text="DELETE", bg=Color3.get(), font=Font1, width=6,
                                command=delete_client)
        self.DeleteBtn.place(width=80, height=32, x=390, y=230)

        self.Clients_scroll_y = Scrollbar(self.ClientsFrame)
        self.Clients_scroll_y.place(width=20, height=174, x=465, y=37)

        self.Clients_scroll_x = Scrollbar(self.ClientsFrame, orient=HORIZONTAL)
        self.Clients_scroll_x.place(width=199, height=20, x=263, y=191)

        self.ClientList = Listbox(self.ClientsFrame, bg=Color2.get(), font=Font3, justify=RIGHT,
                                  yscrollcommand=self.Clients_scroll_y.set, xscrollcommand=self.Clients_scroll_x.set)
        self.ClientList.bind("<<ListboxSelect>>", clients_rec)
        self.ClientList.place(width=200, height=152, x=262, y=36)
        self.Clients_scroll_y.config(command=self.ClientList.yview)
        self.Clients_scroll_x.config(command=self.ClientList.xview)

        self.ProductsFrame = Frame(self.LeftFrame, bg=Color1.get(), bd=2, relief=RIDGE)
        self.ProductsFrame.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH)

        self.Msg = Label(self.ProductsFrame, text="Products Management", bg=Color1.get(), font=Font1)
        self.Msg.place(width=160, height=20, x=10, y=5)

        self.Label = Label(self.ProductsFrame, text="\n", bg=Color1.get(), font=Font2, bd=0)
        self.Label.grid(row=0, column=0, sticky=W)

        self.IDPLabel = Label(self.ProductsFrame, text="ID:", bg=Color1.get(), font=Font2)
        self.IDPLabel.grid(row=1, column=0, sticky=E)

        self.IDPTxt = Entry(self.ProductsFrame, bg=Color2.get(), font=Font1)
        self.IDPTxt.place(width=148, height=23, x=111, y=37)

        self.ProductNameLabel = Label(self.ProductsFrame, text="Name:", bg=Color1.get(), font=Font2)
        self.ProductNameLabel.grid(row=2, column=0, sticky=E)

        self.ProductNameTxt = Entry(self.ProductsFrame, bg=Color2.get(), font=Font1)
        self.ProductNameTxt.place(width=148, height=23, x=111, y=61)

        self.PriceLabel = Label(self.ProductsFrame, text="Price:", bg=Color1.get(), font=Font2)
        self.PriceLabel.grid(row=3, column=0, sticky=E)

        self.PriceTxt = Entry(self.ProductsFrame, bg=Color2.get(), font=Font1)
        self.PriceTxt.place(width=148, height=23, x=111, y=85)

        self.TypeLabel = Label(self.ProductsFrame, text="Type:", bg=Color1.get(), font=Font2)
        self.TypeLabel.grid(row=4, column=0, sticky=E)

        self.TypeDrop = OptionMenu(self.ProductsFrame, Select, *options)
        self.TypeDrop.place(width=148, height=23, x=111, y=112)

        self.StockLabel = Label(self.ProductsFrame, text="Stock:", bg=Color1.get(), font=Font2)
        self.StockLabel.grid(row=5, column=0, sticky=E)

        self.StockTxt = Entry(self.ProductsFrame, bg=Color2.get(), font=Font1)
        self.StockTxt.place(width=148, height=23, x=111, y=139)

        self.CompanyLabel = Label(self.ProductsFrame, text="Company:", bg=Color1.get(), font=Font2)
        self.CompanyLabel.grid(row=6, column=0, sticky=E)

        self.CompanyTxt = Entry(self.ProductsFrame, bg=Color2.get(), font=Font1)
        self.CompanyTxt.place(width=148, height=23, x=111, y=163)

        self.PPhoneLabel = Label(self.ProductsFrame, text="Phone Number:", bg=Color1.get(), font=Font2)
        self.PPhoneLabel.grid(row=7, column=0, sticky=E, pady=(0, 75))

        self.PPhoneTxt = Entry(self.ProductsFrame, bg=Color2.get(), font=Font1)
        self.PPhoneTxt.place(width=148, height=23, x=111, y=187)

        self.ClearBtn = Button(self.ProductsFrame, text="CLEAR", bg=Color3.get(), font=Font1, width=6,
                               command=clear_show_products)
        self.ClearBtn.place(width=80, height=32, x=10, y=230)

        self.SaveBtn = Button(self.ProductsFrame, text="SAVE", bg=Color3.get(), font=Font1, width=6,
                              command=insert_product)
        self.SaveBtn.place(width=80, height=32, x=105, y=230)

        self.UpdateBtn = Button(self.ProductsFrame, text="UPDATE", bg=Color3.get(), font=Font1, width=6,
                                command=update_product)
        self.UpdateBtn.place(width=80, height=32, x=200, y=230)

        self.SearchBtn = Button(self.ProductsFrame, text="SEARCH", bg=Color3.get(), font=Font1, width=6,
                                command=search_product)
        self.SearchBtn.place(width=80, height=32, x=295, y=230)

        self.DeleteBtn = Button(self.ProductsFrame, text="DELETE", bg=Color3.get(), font=Font1, width=6,
                                command=delete_product)
        self.DeleteBtn.place(width=80, height=32, x=390, y=230)

        self.Products_scroll_y = Scrollbar(self.ProductsFrame)
        self.Products_scroll_y.place(width=20, height=174, x=465, y=37)

        self.Products_scroll_x = Scrollbar(self.ProductsFrame, orient=HORIZONTAL)
        self.Products_scroll_x.place(width=199, height=20, x=263, y=191)

        self.ProductList = Listbox(self.ProductsFrame, bg=Color2.get(), font=Font3, justify=RIGHT,
                                   yscrollcommand=self.Products_scroll_y.set, xscrollcommand=self.Products_scroll_x.set)
        self.ProductList.bind("<<ListboxSelect>>", products_rec)
        self.ProductList.place(width=200, height=152, x=262, y=36)
        self.Products_scroll_y.config(command=self.ProductList.yview)
        self.Products_scroll_x.config(command=self.ProductList.xview)

        self.DisplayFrame = Frame(self.RightFrame, width=490, height=580, bg=Color1.get(), bd=2, relief=RIDGE)
        self.DisplayFrame.pack(side=TOP, padx=(0, 5), pady=5, fill=BOTH)

        self.Msg = Label(self.DisplayFrame, text="Transactions", bg=Color1.get(), font=Font1)
        self.Msg.place(width=100, height=20, x=10, y=5)

        self.Msg1 = Label(self.DisplayFrame, text="CLIENT", bg=Color1.get(), font=Font3)
        self.Msg1.place(width=80, height=20, x=20, y=37)

        self.Msg2 = Label(self.DisplayFrame, text="PRODUCT", bg=Color1.get(), font=Font3)
        self.Msg2.place(width=80, height=20, x=123, y=37)

        self.Msg3 = Label(self.DisplayFrame, text="QUANTITY", bg=Color1.get(), font=Font3)
        self.Msg3.place(width=80, height=20, x=216, y=37)

        UserSelected = StringVar()

        self.SelectUser = ttk.Combobox(self.DisplayFrame, state="readonly", width=17, textvariable=UserSelected)
        self.SelectUser["value"] = ()
        values = list(self.SelectUser["value"])
        values.append("")

        c = []
        l1 = d.display_clients()

        for r in range(len(l1)):
            c.append(l1[r][0])

        self.SelectUser["value"] = values + c
        self.SelectUser.current(0)
        self.SelectUser.bind("<<ComboboxSelected>>", c_select)
        self.SelectUser.place(width=100, height=23, x=8, y=61)

        ProductSelected = StringVar()

        self.SelectProduct = ttk.Combobox(self.DisplayFrame, state="readonly", width=17, textvariable=ProductSelected)
        self.SelectProduct["value"] = ()
        values = list(self.SelectProduct["value"])
        values.append("")

        c = []
        l1 = d.display_products()

        for r in range(len(l1)):
            c.append(l1[r][1])

        self.SelectProduct["value"] = values + c
        self.SelectProduct.current(0)
        self.SelectProduct.bind("<<ComboboxSelected>>", p_select)
        self.SelectProduct.place(width=100, height=23, x=111, y=61)

        def q_1(event):
            n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "BackSpace", "Enter", "Escape", "Return", "Space"]
            if event.keysym in n:
                print("NUMBER")
            else:
                cl = messagebox.showwarning("QUANTITY", "Just enter numbers.")
                if cl == "ok":
                    quantity.set(0)

        quantity = IntVar()

        self.QuantitySelect = Entry(self.DisplayFrame, bg=Color2.get(), font=Font1, textvariable=quantity,
                                    justify=CENTER, state=DISABLED)
        self.QuantitySelect.place(width=22, height=23, x=244, y=61)
        self.QuantitySelect.bind("<KeyRelease>", q_1)
        quantity.set(0)

        def left(num):
            if quantity.get() - num == 0:
                quantity.set(0)
                self.ButtonLeft.config(state=DISABLED)
            else:
                quantity.set(quantity.get() - num)

        def right(num):
            if stock.get() > quantity.get():
                quantity.set(quantity.get() + num)
                self.ButtonLeft.config(state=NORMAL)

        self.ButtonLeft = Button(self.DisplayFrame, text="<", font=Font1, bg=Color3.get(), command=lambda: left(1),
                                 state=DISABLED)
        self.ButtonLeft.place(width=29, height=23, x=214, y=61)

        self.ButtonRight = Button(self.DisplayFrame, text=">", font=Font1, bg=Color3.get(), command=lambda: right(1),
                                  state=DISABLED)
        self.ButtonRight.place(width=29, height=23, x=267, y=61)

        self.PurchaseButton = Button(self.DisplayFrame, text="PURCHASE", font=Font1, bg=Color3.get(),
                                     command=insert_purchase)
        self.PurchaseButton.place(width=100, height=45, x=300, y=39)

        self.ClearButton = Button(self.DisplayFrame, text="CLEAR", font=Font1, bg=Color3.get(),
                                  command=clear_show_transactions)
        self.ClearButton.place(width=67, height=45, x=403, y=39)

        self.Tr_scroll_y = Scrollbar(self.DisplayFrame)
        self.Tr_scroll_y.place(width=20, height=169, x=453, y=93)

        self.Tr_scroll_x = Scrollbar(self.DisplayFrame, orient=HORIZONTAL)
        self.Tr_scroll_x.place(width=439, height=20, x=11, y=242)

        self.TrList = Listbox(self.DisplayFrame, bg=Color2.get(), font=Font3, justify=RIGHT,
                              yscrollcommand=self.Tr_scroll_y.set, xscrollcomman=self.Tr_scroll_x.set)
        self.TrList.bind("<<ListboxSelect>>", tr_rec)
        self.TrList.place(width=440, height=147, x=10, y=92)
        self.Tr_scroll_y.config(command=self.TrList.yview)
        self.Tr_scroll_x.config(command=self.TrList.xview)

        self.IDTrLabel = Label(self.DisplayFrame, bg=Color1.get(), font=Font3, text="ID")
        self.IDTrLabel.place(width=80, height=20, x=15, y=270)

        self.IDCliLabel = Label(self.DisplayFrame, bg=Color1.get(), font=Font3, text="CLIENT ID")
        self.IDCliLabel.place(width=100, height=20, x=112, y=270)

        self.IDProLabel = Label(self.DisplayFrame, bg=Color1.get(), font=Font3, text="PRODUCT ID")
        self.IDProLabel.place(width=100, height=20, x=230, y=270)

        self.QuaLabel = Label(self.DisplayFrame, bg=Color1.get(), font=Font3, text="QUANTITY")
        self.QuaLabel.place(width=100, height=20, x=350, y=270)

        self.TotalLabel = Label(self.DisplayFrame, bg="beige", font=Font1, text="TOTAL")
        self.TotalLabel.place(width=83, height=45, x=10, y=335)

        self.IDTrTxt = Entry(self.DisplayFrame, bg=Color2.get(), font=Font1, justify=RIGHT, state=DISABLED)
        self.IDTrTxt.place(width=83, height=20, x=10, y=300)

        self.IDCliTxt = Entry(self.DisplayFrame, bg=Color2.get(), font=Font1, justify=RIGHT, state=DISABLED)
        self.IDCliTxt.place(width=100, height=20, x=111, y=300)

        self.IDProTxt = Entry(self.DisplayFrame, bg=Color2.get(), font=Font1, justify=RIGHT, state=DISABLED)
        self.IDProTxt.place(width=100, height=20, x=229, y=300)

        self.QuaTxt = Entry(self.DisplayFrame, bg=Color2.get(), font=Font1, justify=RIGHT, state=DISABLED)
        self.QuaTxt.place(width=100, height=20, x=348, y=300)

        self.TotalTxt = Entry(self.DisplayFrame, bg=Color2.get(), font=Font3, justify=RIGHT, state=DISABLED)
        self.TotalTxt.place(width=122, height=20, x=100, y=335)

        self.TotalPesosTxt = Entry(self.DisplayFrame, bg=Color2.get(), font=Font3, justify=RIGHT, state=DISABLED)
        self.TotalPesosTxt.place(width=122, height=20, x=100, y=360)

        self.BillButton = Button(self.DisplayFrame, bg=Color3.get(), font=Font1, text="BILLING", state=DISABLED,
                                 command=billing)
        self.BillButton.place(width=100, height=45, x=230, y=336)

        self.DelBillButton = Button(self.DisplayFrame, bg=Color3.get(), font=Font1, text="DELETE", state=DISABLED)
        self.DelBillButton.place(width=100, height=45, x=348, y=336)

        self.Billing = Text(self.DisplayFrame, bg=Color2.get(), font=Font1, state=DISABLED)
        self.Billing.place(width=460, height=170, x=10, y=390)

        show_clients()
        show_products()
        show_transactions()

if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    w = 1000
    h = 600
    s_w = root.winfo_screenwidth()
    s_h = root.winfo_screenheight()
    x_cor = int((s_w/2) - (w/2))
    y_cor = int((s_h/2) - (h/2))
    y_cor -= 30
    root.geometry("{}x{}+{}+{}".format(w, h, x_cor, y_cor))
    app = ManagementSystem(root)
    root.mainloop()

"""
d.insert_genders(1, "MALE")
d.insert_genders(2, "FEMALE")
d.insert_types(1, "GUITAR")
d.insert_types(2, "BASS GUITAR")
d.insert_types(3, "PIANO")
d.insert_types(4, "MICROPHONE")
d.insert_types(5, "DRUMS")
"""
