import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import datetime
import PIL.Image
import PIL.ImageTk
import mysql.connector



#my modules
import Man_st as ms
import Man_em as me

import View_Students as VS
import View_Employee as VE

import tkinter.tix as tix 



conn = mysql.connector.connect(host = 'localhost', database = 'school_management', user = 'root', password = 'Kushal@2006',auth_plugin='mysql_native_password')

cur = conn.cursor()

class dash_board():
    def __init__(self, root):
        self.root = root
        
        self.style = ttk.Style()
        
        self.frame1 = tk.Frame(root, height = 737, width =250, bg = 'white', cursor = 'hand2')
        self.frame1.place(x = 0, y = 136)

        self.hm = PIL.Image.open('homeji.png')
        self.hm = self.hm.resize((240, 90))
        self.home_im = PIL.ImageTk.PhotoImage(self.hm)
        
        self.Home_btn = ttk.Button(self.frame1, image = self.home_im)
        self.Home_btn.place(x = 0, y = 0, height = 100, width = 250)

        self.st_im = PIL.Image.open('student1.png')
        self.st_im = self.st_im.resize((240,91))

        self.stu_ic = PIL.ImageTk.PhotoImage(self.st_im)

        self.Students = ttk.Button(self.frame1, image = self.stu_ic,command = self.Mana_Stu)
        self.Students.place(x = 0, y = 100, width = 250, height = 100)
        
        self.em_im = PIL.Image.open('Employee.png')
        self.em_im = self.em_im.resize((242,90))

        self.emp_ic = PIL.ImageTk.PhotoImage(self.em_im)

        self.Employee = ttk.Button(self.frame1,image = self.emp_ic, command = self.mana_emp)
        self.Employee.place(x = 0, y = 200, width = 250, height = 100)

        self.stu_in = PIL.Image.open('student-info.png')
        self.stu_in = self.stu_in.resize((242,90))

        self.stu_inf_ic = PIL.ImageTk.PhotoImage(self.stu_in)

        self.ViewStudents = ttk.Button(self.frame1,image = self.stu_inf_ic, command = self.view_students_comm)
        self.ViewStudents.place(x = 0, y = 300, width = 250, height = 100)

        self.emp_in = PIL.Image.open('employee_de.png')
        self.emp_in = self.emp_in.resize((240,90))

        self.emp_inf_ic = PIL.ImageTk.PhotoImage(self.emp_in)

        self.ViewEmployee = ttk.Button(self.frame1, image = self.emp_inf_ic, command = self.view_employee_comm)
        self.ViewEmployee.place(x = 0, y = 400,width = 250,height=100)

        self.clas_ic = PIL.Image.open('classroom.png')
        self.clas_ic = self.clas_ic.resize((242,90))

        self.class_ro_ic = PIL.ImageTk.PhotoImage(self.clas_ic)

        self.Class_ma = ttk.Button(self.frame1, image = self.class_ro_ic)
        self.Class_ma.place(x=0, y = 500, width = 250, height = 100)

        self.exi_ic = PIL.Image.open('EXIT.png')
        self.exi_ic = self.exi_ic.resize((240,90))

        self.exi_icon_ = PIL.ImageTk.PhotoImage(self.exi_ic)

        self.Exit = ttk.Button(self.frame1,command = exit, image = self.exi_icon_)
        self.Exit.place(x = 0, y = 600,width = 250,height = 100)


        self.f2 = tk.Frame(root, height = 137, width = 2000, bg = 'white')
        self.f2.place(x = 0, y = 0)
        self.label = tk.Label(self.f2, text = 'SCHOOL MANAGEMENT SYSTEM', anchor = tk.CENTER, font = ('Arial 50 bold'), bg = 'white')
        self.label.place(x = 230, y = 20)


        self.LogOut = tk.Button(self.f2, text = 'LogOut',command=self.LogOuuut, bg = 'white', activebackground = 'white', borderwidth = 0, font = 'Arial 20 underline bold', activeforeground = 'red', cursor = 'hand2')
        self.LogOut.place(x = 1350, y = 50, width = 200)

        self.LogOut.bind('<Enter>', func= lambda a: self.LogOut.config(foreground = 'red'))
        self.LogOut.bind('<Leave>', func=  lambda a: self.LogOut.config(foreground = 'black'))


        self.frame2 = tk.Frame(root, height = 700, width = 1350, bg = 'black')

        self.frame2.place(x = 250, y = 136)

        # self.label3 = tk.Label(self.frame2, text = 'hello', fg=  'white', bg = 'black', font = ('Arial', 20))
        # self.label3.place(x = 125, y = 25)


        sep = ttk.Separator(self.frame2, orient = 'horizontal')
        sep.place(x = 0, y = 40, width = 1350)


    def Mana_Stu(self):

        self.frame2.destroy()
        self.frame2 = tk.Frame(root, height = 700, width = 1350, bg = 'black')

        self.frame2.place(x = 250, y = 136)


        ms.Mana_st1(self.frame2)

        self.frame3 = tk.Frame(self.frame2, height = 35, width = 1350, bg = 'black')
        self.frame3.place(x = 0, y = 0)

        self.label_path = tk.Label(self.frame3, text = 'Manage Students', font = ('Arial', 20), fg = 'white', bg = 'black')
        self.label_path.place(x = 0, y = 0)

        
            

    def LogOuuut(self):
        self.root.destroy()


    def mana_emp(self):

        self.frame2.destroy()
        self.frame2 = tk.Frame(root, height = 700, width = 1350, bg = 'black')

        self.frame2.place(x = 250, y = 136)

        me.Man_em1(self.frame2)

        self.frame3 = tk.Frame(self.frame2, height = 35, width = 1350, bg = 'black')
        self.frame3.place(x = 0, y = 0)

        self.label_path = tk.Label(self.frame3, text = 'Manage Employees', font = ('Arial', 20), fg = 'white', bg = 'black')
        self.label_path.place(x = 0, y = 0)


    def view_students_comm(self):

        self.frame2.destroy()
        self.frame2 = tk.Frame(root, height = 700, width = 1350, bg = 'black')

        self.frame2.place(x = 250, y = 136)

        VS.View_stu(self.frame2)

        self.frame3 = tk.Frame(self.frame2, height = 35, width = 1350, bg = 'black')
        self.frame3.place(x = 0, y = 0)

        self.label_path = tk.Label(self.frame3, text = 'View Students', font = ('Arial', 20), fg = 'white', bg = 'black')
        self.label_path.place(x = 0, y = 0)

    def view_employee_comm(self):

        self.frame2.destroy()
        self.frame2 = tk.Frame(root, height = 700, width = 1350, bg = 'black')

        self.frame2.place(x = 250, y = 136)

        VE.View_employee(self.frame2)
        self.frame3 = tk.Frame(self.frame2, height = 35, width = 1350, bg = 'black')
        self.frame3.place(x = 0, y = 0)
        
        self.label_path = tk.Label(self.frame3, text = 'View Employee', font = ('Arial', 20), fg = 'white', bg = 'black')
        self.label_path.place(x = 0, y = 0)





    
root = tk.tix.Tk()

a = dash_board(root)

root.mainloop()