import tkinter as tk
import base64
from PIL import Image
import io
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
import io
import numpy as np
from tkscrolledframe import ScrolledFrame

class View_employee():

    def __init__(self, frame_name):

        self.conn = mysql.connector.connect(host = 'localhost', database = 'school_management', user = 'root', password = 'Kushal@2006',charset='utf8')
        self.cur = self.conn.cursor()

        self.frame_name = frame_name

        self.frame1 = tk.Frame(frame_name, bg = 'yellow')
        self.canvas_scrolling = tk.Canvas(self.frame1, bg = 'red')
        self.Y_ScroolBar = ttk.Scrollbar(self.frame1, orient = 'vertical', command = self.canvas_scrolling.yview)
        self.profile_frame = tk.Frame(self.canvas_scrolling, width = 1335, height = 650)

        self.profile_frame.bind("<Configure>",lambda e: self.canvas_scrolling.configure(scrollregion=self.canvas_scrolling.bbox("all")))

        #self.canvas_scrolling.create_window((0, 0), window=self.profile_frame, anchor="nw")

        #self.canvas_scrolling.configure(yscrollcommand=self.Y_ScroolBar.set)

        self.frame1.pack(fill = 'both', expand = 1, padx = 0, pady = 45)
        self.canvas_scrolling.pack(side = tk.LEFT,fill = 'both', expand = 1)

        # self.Y_ScroolBar.place(x = 1332, y= 10, height = 620)
        # self.profile_frame.place(x = 0, y = 0)



        #self.ve_label()

    def ve_label(self):

        


        self.cur.execute('select ROW_NUMBER() Over (Order by employee_table.employee_id) AS SN,employee_table.employee_id, employee_table.Employee_Name, job_tabel.Job, employee_table.Gender,employee_table.Date_of_birth,employee_details.Father_name, employee_contact.Phone_number,employee_contact.E_mail,employee_address.address, employee_profile.employee_photo from (((((employee_table inner join employee_address on  employee_address.employee_id = employee_table.employee_id) inner join employee_details on  employee_details.employee_id = employee_table.employee_id) inner join employee_contact on  employee_contact.employee_id = employee_table.employee_id) inner join job_tabel on job_tabel.employee_id = employee_table.employee_id) inner join employee_profile on employee_profile.employee_id = employee_table.employee_id) order by employee_table.employee_id asc;')



        rows = self.cur.fetchall()

        Name_list = []
        Job_list = []
        Gender_list = []
        D_O_B_list = []
        photo_list = []

        for record in rows:

            Sn = record[0]
            Name1 = record[2]
            
            Job1 = record[3]
            Gender1 = record[4]
            D_O_B1 = record[5]
            photo1 = record[10]

            Name_list.append(Name1)
            Job_list.append(Job1)
            Gender_list.append(Gender1)
            D_O_B_list.append(D_O_B1)
            photo_list.append(photo1)


        xa = 10
        ya = 10

        try:

            for i in range(Sn):

                self.profile_box = tk.LabelFrame(self.profile_frame, height = 250, width = 450)
                self.profile_box.place(x = xa, y = ya)

                self.photo_box = tk.LabelFrame(self.profile_box, width = 200,height = 240)
                self.photo_box.place(x = 5, y = 2)

                self.Name_lab = tk.Label(self.profile_box, text = '     Name:', font = 'Arial 15 bold')
                self.Name_lab.place(x = 210, y = 10)

                self.Job_lab = tk.Label(self.profile_box, text = '        Job:', font = 'Arial 15 bold')
                self.Job_lab.place(x = 210, y = 60)

                self.Gender_lab = tk.Label(self.profile_box, text = '  Gender:', font = 'Arial 15 bold')
                self.Gender_lab.place(x = 210, y = 110)

                self.D_O_B_lab = tk.Label(self.profile_box, text = '    D.O.B:', font = 'Arial 15 bold')
                self.D_O_B_lab.place(x = 210, y = 160)

                xa += 450

                if xa > 900:
                    xa = 10
                    ya += 270
                
                Name = Name_list[i]
                Job = Job_list[i]
                Gender = Gender_list[i]
                D_O_B = D_O_B_list[i]
                photo = photo_list[i]



                self.Name_ent = tk.Label(self.profile_box, text = Name, font = 'Arial 15')
                self.Name_ent.text = Name
                self.Name_ent.place(x = 310, y = 10)

                self.Job_ent = tk.Label(self.profile_box, text = Job, font = 'Arial 15')
                self.Job_ent.text = Name
                self.Job_ent.place(x = 310, y = 60)

                self.Gender_ent = tk.Label(self.profile_box, text = Gender, font = 'Arial 15')
                self.Gender_ent.text = Gender
                self.Gender_ent.place(x = 310, y = 110)

                self.D_O_B_ent = tk.Label(self.profile_box, text =  D_O_B, font = 'Arial 15')
                self.D_O_B_ent.text = D_O_B
                self.D_O_B_ent.place(x = 310, y = 160)

                img_encoded = base64.b64encode(photo)
                photo1 = tk.PhotoImage(data = img_encoded)

                self.Phto_img = tk.Label(self.profile_box, image =  photo1, font = 'Arial 15')
                self.Phto_img.image = photo1
                self.Phto_img.place(x = 7, y = 3)

        except UnboundLocalError:
            messagebox.showinfo('View Students', 'No students')