import tkinter as tk
import base64
from PIL import Image
import io
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
import io
import numpy as np


class View_stu():

    def __init__(self, frame_name):

        self.conn = mysql.connector.connect(host = 'localhost', database = 'school_management', user = 'root', password = 'Kushal@2006',charset='utf8')
        self.cur = self.conn.cursor()

        self.frame_name = frame_name
        
        self.profile_frame = tk.Frame(frame_name, bg = 'white')
        self.profile_frame.place(x = 0 , y = 45, width = 1350, height = 700)





        self.vs_label()

    def vs_label(self):


        self.cur.execute('SELECT ROW_NUMBER() Over (Order by student_table.student_id) AS SN, student_table.student_id, student_table.Student_name, student_table.Class ,student_table.Gender,student_details.father_name, student_details.mother_name, student_details.date_of_birth , contact_table.phone_no, contact_table.e_mail, address_table.address, student_profile.profile_photo from ((((student_table inner join student_details on student_table.student_id = student_details.student_id) inner join contact_table on student_table.student_id = contact_table.student_id) inner join address_table on student_table.student_id = address_table.student_id) inner join student_profile on student_table.student_id = student_profile.student_id);')



        rows = self.cur.fetchall()

        Name_list = []
        Class_list = []
        Gender_list = []
        D_O_B_list = []
        photo_list = []

        for record in rows:

            Sn = record[0]
            Name1 = record[2]
            
            Class1 = record[3]
            Gender1 = record[4]
            D_O_B1 = record[7]
            photo1 = record[11]

            Name_list.append(Name1)
            Class_list.append(Class1)
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

                self.Name_lab = tk.Label(self.profile_box, text = '   Name:', font = 'Arial 15 bold')
                self.Name_lab.place(x = 210, y = 10)

                self.Class_lab = tk.Label(self.profile_box, text = '   Class:', font = 'Arial 15 bold')
                self.Class_lab.place(x = 210, y = 60)

                self.Gender_lab = tk.Label(self.profile_box, text = 'Gender:', font = 'Arial 15 bold')
                self.Gender_lab.place(x = 210, y = 110)

                self.D_O_B_lab = tk.Label(self.profile_box, text = '  D.O.B:', font = 'Arial 15 bold')
                self.D_O_B_lab.place(x = 210, y = 160)

                xa += 450

                if xa > 1000:
                    xa = 10
                    ya += 270
                
                Name = Name_list[i]
                Class = Class_list[i]
                Gender = Gender_list[i]
                D_O_B = D_O_B_list[i]
                photo = photo_list[i]



                self.Name_ent = tk.Label(self.profile_box, text = Name, font = 'Arial 15')
                self.Name_ent.text = Name
                self.Name_ent.place(x = 310, y = 10)

                self.Class_ent = tk.Label(self.profile_box, text = Class, font = 'Arial 15')
                self.Class_ent.text = Name
                self.Class_ent.place(x = 310, y = 60)

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
                self.Phto_img.place(x = 30, y = 15)

        except UnboundLocalError:
            messagebox.showinfo('View Students', 'No students')
                


# root = tk.Tk()
# View_stu(root)
# root.mainloop()









        # self.pho = tk.Label(self.a)
        # self.pho.place(x = 3, y = 2)

        # self.b = tk.Label(self.a, text = 'Name:', font = 'Arial 15 bold')
        # self.b.place(x = 150, y = 2)

        # self.c = tk.Label(self.a, text = 'Class', font = 'Arial 15 bold')
        # self.c.place(x = 150, y = 40)


        # Val = str(name)

        # self.Name_val = tk.Label(self.a, text = Val, font = 'Arial 15')
        # self.Name_val.place(x = 220, y = 2)

        # self.a.bind('<Double-Click>')














