import sqlite3


class Database:
    @staticmethod
    def conn():
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists gender (
                    id_gender integer primary key,
                    gender text
                )""")
        c.execute("""CREATE TABLE if not exists type (
                    id_type integer primary key,
                    type text
                )""")
        c.execute("""CREATE TABLE if not exists clients (
                            id_c integer primary key,
                            name_c text,
                            address text,
                            id_gender integer,
                            birthday text,
                            phone_c text,
                            email text
                        )""")
        c.execute("""CREATE TABLE if not exists products (
                                    id_p integer primary key,
                                    name_p text,
                                    price text,
                                    id_type integer,
                                    stock text,
                                    company text,
                                    phone_p text
                                )""")
        c.execute("""CREATE TABLE if not exists transactions (
                                    id_t integer primary key,
                                    id_c integer,
                                    id_p integer,
                                    quantity integer
                                )""")
        conn.commit()
        conn.close()
        print("DATABASE CONNECTED.")

    @staticmethod
    def insert_genders(i, t):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = "INSERT INTO gender VALUES (?, ?)"
        c.execute(query, (i, t))
        conn.commit()
        conn.close()
        print("GENDER " + str(i) + " CREATED")

    @staticmethod
    def insert_types(i, t):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = "INSERT INTO type VALUES (?, ?)"
        c.execute(query, (i, t))
        conn.commit()
        conn.close()
        print("TYPE " + str(i) + " CREATED")

    @staticmethod
    def insert_client(idc, name, address, gender, bir, phone, email):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = "INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?, ?)"
        c.execute(query, (idc, name, address, gender, bir, phone, email))
        conn.commit()
        conn.close()
        print("CLIENT " + name + " INSERTED.")

    @staticmethod
    def show_type():
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = "SELECT * FROM type"
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows

    @staticmethod
    def insert_product(idp, name, price, idtype, stock, company, phone):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = "INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?)"
        c.execute(query, (idp, name, price, idtype, stock, company, phone))
        conn.commit()
        conn.close()
        print("PRODUCT " + name + " INSERTED.")

    @staticmethod
    def show_clients():
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = "SELECT name_c, gender, birthday, phone_c, id_c " \
                "FROM clients cl, gender gd WHERE cl.id_gender=gd.id_gender"
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows
        
    @staticmethod
    def show_products():
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = "SELECT name_p, price, type, stock, id_p FROM products pr, type tp WHERE pr.id_type=tp.id_type"
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows

    @staticmethod
    def select_client(id_c):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = "SELECT * FROM clients WHERE id_c=?"
        c.execute(query, (id_c, ))
        row = c.fetchall()
        conn.commit()
        conn.close()
        return row

    @staticmethod
    def select_product(id_p):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = "SELECT * FROM products WHERE id_p=?"
        c.execute(query, (id_p,))
        row = c.fetchall()
        conn.commit()
        conn.close()
        return row

    @staticmethod
    def delete_client(id_c):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = "DELETE FROM clients WHERE id_c=?"
        c.execute(query, (id_c, ))
        conn.commit()
        conn.close()
        print(str(id_c) + " DELETED.")

    @staticmethod
    def delete_product(id_p):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = "DELETE FROM products WHERE id_p=?"
        c.execute(query, (id_p,))
        conn.commit()
        conn.close()
        print(str(id_p) + " DELETED.")

    @staticmethod
    def search_client(idc="", name="", address="", phone="", email=""):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = ("""
                    SELECT 
                        name_c, birthday, phone_c, id_c  \
                    FROM 
                        clients  \
                    WHERE 
                        id_c=? or name_c=? or address=? or phone_c=? or email=?
                """)
        c.execute(query, (idc, name, address, phone, email))
        rows = c.fetchall()
        conn.commit()
        conn.close()
        print("CLIENT SELECTED.")
        return rows

    @staticmethod
    def search_product(idp="", name="", company=""):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = ("""
                    SELECT 
                        id_p, name_p, price, stock   \
                    FROM 
                        products  \
                    WHERE 
                        id_p=? or name_p=? or company=?
                    """)
        c.execute(query, (idp, name, company))
        rows = c.fetchall()
        conn.commit()
        conn.close()
        print("PRODUCT SELECTED.")
        return rows

    @staticmethod
    def display_clients():
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = ("""
                    SELECT
                        name_c, id_c
                    FROM
                        clients
                """)
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows

    @staticmethod
    def display_products():
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = ("""
                    SELECT
                            id_p, name_p
                    FROM
                            products
                """)
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows

    @staticmethod
    def select_ps(pid):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = ("""
                    SELECT
                        price, stock
                    FROM 
                        products
                    WHERE
                        id_p=?                
                """)
        c.execute(query, (pid, ))
        row = c.fetchall()
        conn.commit()
        conn.close()
        return row

    @staticmethod
    def insert_purchase(idt, idc, idp, quantity):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = "INSERT INTO transactions VALUES (?, ?, ?, ?)"
        c.execute(query, (idt, idc, idp, quantity))
        conn.commit()
        conn.close()
        print("TRANSACTION " + str(idt) + " INSERTED.")

    @staticmethod
    def show_transactions():
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = """ 
                    SELECT 
                        id_t, name_c, email, phone_c, name_p, quantity 
                    FROM 
                        clients cl, products pd, transactions tr 
                    WHERE 
                        tr.id_c=cl.id_c
                    AND
                        tr.id_p=pd.id_p
                """
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows

    @staticmethod
    def select_purchase(tid):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = ("""
                    SELECT
                        *
                    FROM 
                        transactions
                    WHERE
                        id_t=?                
                """)
        c.execute(query, (tid,))
        row = c.fetchall()
        conn.commit()
        conn.close()
        return row

    @staticmethod
    def get_price(pid):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = ("""
                    SELECT
                        price, company, name_p
                    FROM
                        products
                    WHERE
                        id_p=?    
                """)
        c.execute(query, (pid, ))
        row = c.fetchall()
        conn.commit()
        conn.close()
        return row

    @staticmethod
    def get_client(cid):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = ("""
                    SELECT
                        *
                    FROM
                        clients
                    WHERE id_c=?
                """)
        c.execute(query, (cid, ))
        row = c.fetchall()
        conn.commit()
        conn.close()
        return row

    @staticmethod
    def get_gender(gid):
        conn = sqlite3.connect("Database/management.db")
        c = conn.cursor()
        query = ("""
                    SELECT
                        gender
                    FROM
                        gender
                    WHERE id_gender=?
                """)
        c.execute(query, (gid, ))
        row = c.fetchall()
        conn.commit()
        conn.close()
        return row
