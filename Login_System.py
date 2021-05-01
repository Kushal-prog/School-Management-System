from tkinter import *
from tkinter import messagebox
import MySQLdb
from DashBoard import *


class Login():
    def __init__(self, root, *args):
        global Username
        global Password

        self.root = root
        self.f1 = Frame(root, height =200, width = 170)
        self.f1.grid()
        self.Username_label = Label(self.f1, text = 'Username')
        self.Username_label.grid(row=1, column = 0)
        self.Password_Label = Label(self.f1, text = 'Password')
        self.Password_Label.grid(row=2, column = 0)

        self.Username_Entry = Entry(self.f1)
        self.Username_Entry.grid(row=1, column=1)
        self.Password_Entry = Entry(self.f1, show = '*')
        self.Password_Entry.grid(row=2, column=1)
        self.submit = Button(self.f1, text = 'Submit', command = self.Submit)
        self.submit.grid(row = 3,column = 0)
        Username = self.Username_Entry.get()
        Password = self.Password_Entry.get()

    def Submit(self):
        Username = self.Username_Entry.get()
        Password = self.Password_Entry.get()


        if Username == '' or Password == '':
            messagebox.showinfo('Empty box', 'Empty fields are not allowed', parent = self.root)
        else:                 

            conn = MySQLdb.connect(host='localhost', user = 'root', password = 'Kushal@2006', db='school_mana')
            cur = conn.cursor()
            cur.execute(f"select * from login_emp where ")
            row = cur.fetchone()
            print(row)
        
            if row == None:
                messagebox.showerror('Incorrect Username or Password','Incorrect Username or Password')
            else:
                self.root.destroy()
                root = Tk()
                a = dash_board(root)

