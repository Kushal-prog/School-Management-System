import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import mysql.connector
from datetime import datetime
from PIL import ImageTk, Image
import keyboard
from tkinter import messagebox
from tkinter import filedialog
import io
from datetime import datetime



class Mana_st1():

    def __init__(self, frame_nam):

        self.frame_nam = frame_nam

        self.style = ttk.Style()

        self.style.theme_settings("default", {"TNotebook.Tab": {"configure": {"padding": [30, 100]}}})

        self.note = ttk.Notebook(frame_nam, style = 'TNotebook')
        
        self.f3 = tk.LabelFrame(self.frame_nam, height = 700, width = 1350, labelanchor = tk.N, font = 'Arial 50', bg = 'black')


        self.note.add(self.f3, text = '                         Edit                        ', padding = 5)
        self.note.place(x = 0, y = 45)


        self.conn = mysql.connector.connect(host = 'localhost', database = 'school_management', user = 'root', password = 'Kushal@2006',charset='utf8', auth_plugin = 'mysql_native_password')
        self.cur = self.conn.cursor(buffered = True)






        #call the label function
        self.stu_lab()

        #call the entry function
        self.stu_ent()

        #call the buttons function
        self.stu_Button()

        #call the student lists function
        self.student_li()


















# Fnction for labels
    def stu_lab(self):

        self.Name_lab = tk.Label(self.f3, text = 'Name:', font = 'Arial 20', bg = 'black', fg= 'white')
        self.Name_lab.place(x = 5, y = 5)

        
        
        self.stu_id_lab = tk.Label(self.f3, text = 'Student ID:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.stu_id_lab.place(x = 5, y = 55)

        
    
 
        self.Class_lab = tk.Label(self.f3, text = 'Class:', font = 'Arial 20',bg = 'black', fg = 'white')
        self.Class_lab.place(x = 5, y = 100)

        

        self.Gender_lab = tk.Label(self.f3, text = 'Gender:', font = 'Arial 20', bg = 'black', fg = 'white')

        self.Gender_lab.place(x = 290, y = 100)

        

        self.Date_lab = tk.Label(self.f3, text = 'D.O.B:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.Date_lab.place(x = 5, y = 150)

        
        self.phone_no = tk.Label(self.f3, text = 'Phone No:', font = 'Arial 20', bg = 'black', fg = 'white')

        self.phone_no.place(x = 5, y = 300)

        

        self.E_mail_lab = tk.Label(self.f3, text = 'E-Mail:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.E_mail_lab.place(x = 10, y = 350)

        


        self.Fath_lab = tk.Label(self.f3, text = 'Father Name:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.Fath_lab.place(x = 5 , y = 200)


        self.mother_lab = tk.Label(self.f3, text = 'Mother Name:', font = 'Arial 20', bg = 'black', fg = 'white')

        self.mother_lab.place(x = 5, y = 250)

        

        self.Adress_lab = tk.Label(self.f3, text = 'Address: ', font = 'Arial 20', bg = 'black', fg = 'white')
        self.Adress_lab.place(x = 5, y = 400)

        self.Upload_lab = tk.Label(self.f3, text = 'Upload Photo:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.Upload_lab.place(x = 5, y = 520)
        




















#functions for entry, combobox widgets
    def stu_ent(self):

        




        self.Name_ent = ttk.Entry(self.f3, font= 'Arial 19 ')
        self.callback1 = self.f3.register(self.only_string_input)
        self.Name_ent.configure(validate = "key", validatecommand =(self.callback1, "%P"))

        self.Name_ent.place(x = 200, y = 15, height = 35, width = 350)



        self.stu_id_ent = ttk.Entry(self.f3, font= 'Arial 20 ')
        self.callback = self.f3.register(self.only_numeric_input)
        self.stu_id_ent.configure(validate = "key", validatecommand =(self.callback, "%P"))

        self.stu_id_ent.place(x = 200, y = 60, height = 35, width = 350)


        
        self.select_CLass = tk.StringVar()

        self.Class_ent = ttk.Combobox(self.f3, font= 'Arial 20 ', textvariable = self.select_CLass, state ='readonly')

        self.Class_ent['values'] = ('1ˢᵗ',
                                    '2ⁿᵈ',
                                    '3ʳᵈ',
                                    '4ᵗʰ',
                                    '5ᵗʰ',
                                    '6ᵗʰ',
                                    '7ᵗʰ',
                                    '8ᵗʰ',
                                    '9ᵗʰ',
                                    '10ᵗʰ',
                                    '11ᵗʰ',
                                    '12ᵗʰ'
                                        )

        self.Class_ent.place(x = 200, y = 100, width = 90)


        select_Gender = tk.StringVar()
        self.Gender_ent = ttk.Combobox(self.f3, font = 'Arial 20', textvariable = select_Gender, state ='readonly')        
        self.Gender_ent['values'] = ('Male', 'Female', 'Other')
        self.Gender_ent.place(x = 400, y = 100, width = 150)


        self.Date = DateEntry(self.f3,width=20,background="darkblue",fg="white",year=2021,font = 'Arial 20', state = 'readonly')
        self.Date.place(x = 200, y = 150, width = 350)


        select_cc = tk.IntVar()
        self.ph_cc = ttk.Combobox(self.f3, font = 'Arial 20', textvariable = select_cc, values = ('+91','+62'), state ='readonly')

        self.ph_cc.place(x = 200, y = 300, width = 80)

        self.ph_ent = ttk.Entry(self.f3, font= 'Arial 20 ')

        self.callback2 = self.callback = self.f3.register(self.only_numeric_input_phone)

        self.ph_ent.configure(validate = "key", validatecommand =(self.callback2, "%P"))

        self.ph_ent.place(x = 280, y = 300, width = 270)



        self.E_mail_ent = tk.Entry(self.f3, font = 'Arial 20')
        self.E_mail_ent.place(x = 200, y = 350, width = 350)



        self.Fath_ent = ttk.Entry(self.f3, font= 'Arial 20')
        self.Fath_ent.place(x = 200, y = 200, width = 350)



        self.mother_ent = ttk.Entry(self.f3, font = 'Arial 20')
        self.mother_ent.place(x = 200, y = 250, width = 350)



        self.Adress_ent = tk.Text(self.f3 ,font = 'Arial')
        self.Adress_ent.place(x = 200, y = 400, height = 100, width = 350)
























#function to display student lists 
    def student_li(self):


        self.sep_er = ttk.Separator(self.f3, orient = 'vertical')
        self.sep_er.place(x = 600, y = 0, height = 700)
        
        

        self.student_list = ttk.Treeview(self.f3)
        self.st_sc_v = ttk.Scrollbar(self.student_list,orient = 'vertical', command = self.student_list.yview)
        self.st_sc_h = ttk.Scrollbar(self.student_list,orient = 'horizontal', command = self.student_list.xview)

        self.student_list.configure(yscrollcommand = self.st_sc_v.set)
        self.student_list.configure(xscrollcommand = self.st_sc_h.set)

        self.student_list.place(x = 610, y = 100, width = 730, height = 500)
        self.st_sc_v.pack(side = tk.RIGHT, fill = tk.Y)
        self.st_sc_h.pack(side = tk.BOTTOM, fill = tk.X)

        
        self.student_list['column'] = ('Sn', 'Student ID','Name' ,'Class', 'Gender', 'D.O.B', 'Father Name', 'Mother Name', 'Phone No', 'E-mail', 'Address', 'Photo', 'Face ID')

        
        self.student_list.column('#0', width=0,stretch=tk.NO)
        self.student_list.column('Sn', anchor = tk.W, width = 20)
        self.student_list.column('Student ID',anchor=tk.CENTER ,width=80)
        self.student_list.column('Name',anchor=tk.W ,width=120)
        
        self.student_list.column('Class', anchor=tk.W,width=80)
        self.student_list.column('E-mail', anchor=tk.W,width=80)
        self.student_list.column('Gender', anchor=tk.W,width=80)
        self.student_list.column('D.O.B', anchor = tk.W, width=80)

        self.student_list.column('Father Name', anchor = tk.W, width=80)
        self.student_list.column('Mother Name', anchor = tk.W, width=80)

        self.student_list.column('Phone No', anchor = tk.W, width=80)

        self.student_list.column('Address', anchor = tk.W, width=80)
        self.student_list.column('Photo', anchor = tk.W, width=80)
        self.student_list.column('Face ID', anchor = tk.W, width=80)



        self.student_list.heading('#0',text='', anchor= tk.W)
        self.student_list.heading('Sn', text = 'Sn', anchor = tk.CENTER)
        

        self.student_list.heading('Student ID',text='Student ID', anchor=tk.W)
        self.student_list.heading('Name', text='Name', anchor=tk.CENTER)

        self.student_list.heading('Class',text='Class', anchor=tk.W)
        

        self.student_list.heading('Gender',text='Gender', anchor=tk.W)

        self.student_list.heading('D.O.B', text = 'Date of Birth', anchor = tk.W)

        self.student_list.heading('Father Name', text = 'Father Name', anchor=tk.W)

        self.student_list.heading('Mother Name', text = 'Mother Name', anchor = tk.W)

        self.student_list.heading('Phone No', text = 'Phone No', anchor = tk.W)

        self.student_list.heading('E-mail',text='E-mail', anchor=tk.W)

        self.student_list.heading('Address', text='Address', anchor=tk.W)

        self.student_list.heading('Photo', text='Photo', anchor=tk.W)
        self.student_list.heading('Face ID', text = 'Face ID', anchor = tk.W)

        self.cur.execute('SELECT ROW_NUMBER() Over (Order by student_table.student_id) AS SN, student_table.student_id, student_table.Student_name, student_table.Class ,student_table.Gender,  student_details.date_of_birth ,student_details.father_name, student_details.mother_name,contact_table.phone_no, contact_table.e_mail, address_table.address, student_profile.profile_photo from ((((student_table inner join student_details on student_table.student_id = student_details.student_id) inner join contact_table on student_table.student_id = contact_table.student_id) inner join address_table on student_table.student_id = address_table.student_id) inner join student_profile on student_table.student_id = student_profile.student_id);')

        rows = self.cur.fetchall()

        self.count = 0

        for row in rows:
            self.student_list.insert(parent='', index='end',iid = self.count, text='Parent', values=(row))

            self.count += 1
 



        
        self.style.configure('TButton', font = 'Arial 20', foreground  = 'red', background = 'blue', borderwidth = 10)
        self.style.map('TButton', foreground = [('active', 'red'), ('pressed', 'red')], background = [('active', 'red'), ('pressed', 'red')])


        self.Search_d_lab = tk.Label(self.f3, text = 'Search By:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.Search_d_lab.place(x = 610, y= 10)

        search_value = tk.StringVar()

        self.Search_d_combo = ttk.Combobox(self.f3, font = 'Arial 20', textvariable = search_value, state = 'readonly')
        
        self.Search_d_combo['values'] = (
            'Name',
            'Roll_no', 
            'E-mail',
            'Phone No'
            )

        self.Search_d_combo.place(x = 770, y= 10, width = 150)

        self.search_ent = ttk.Entry(self.f3, font= 'Arial 20')
        self.search_ent.place(x = 930, y = 10, width = 170)

        self.search_but = ttk.Button(self.f3, text = 'Search')
        self.search_but.place(x = 1150, y = 10, width = 125)

        self.showall = ttk.Button(self.f3, text = 'Show All')
        self.showall.place(x = 610, y = 50, height = 40)

        self.student_list.bind('<ButtonRelease - 1>', self.selected)


    def selected(self, event):

        self.Name_ent.delete(0, tk.END)
        self.stu_id_ent.delete(0, tk.END)
        self.Class_ent.set('')
        self.Gender_ent.set('')
        self.mother_ent.delete(0, tk.END)

        ab = datetime.now()

        date_now = ab.strftime("%x")


        self.Date.set_date(date_now)

        self.ph_cc.set('')
        self.ph_ent.delete(0, tk.END)

        self.E_mail_ent.delete(0, tk.END)
        self.Fath_ent.delete(0, tk.END)
        self.Adress_ent.delete(1.0, tk.END)

        selected = self.student_list.focus()
        values_employee_list = self.student_list.item(selected, 'values')


        self.Name_ent.insert(0, values_employee_list[2])
        self.stu_id_ent.insert(0, values_employee_list[1])
        self.Class_ent.set(values_employee_list[3])
        self.Gender_ent.set(values_employee_list[4])
        Phone_number_list = []

        for Phone_number_ in values_employee_list[8]:
            Phone_number_list.append(Phone_number_)

        Phone_number_code = Phone_number_list[0] + Phone_number_list[1] + Phone_number_list[2]
        a = Phone_number_list[3: len(Phone_number_list) + 1]
        a = "".join(a)

        self.ph_cc.set(Phone_number_code)
        self.ph_ent.insert(0, a)


        self.E_mail_ent.insert(0, values_employee_list[9])
        self.Fath_ent.insert(0, values_employee_list[6])
        self.mother_ent.insert(0, values_employee_list[7])
        self.Adress_ent.insert(1.0, values_employee_list[10])







#function to display buttons
    def stu_Button(self):


        self.style.configure('TButton', font = 'Arial 20', foreground  = 'red', background = 'blue', borderwidth = 10)
        
        self.style.map('TButton', foreground = [('active', 'red'), ('pressed', 'red')], background = [('active', 'red'), ('pressed', 'red')])

        self.Upload = ttk.Button(self.f3, text = 'Select Photo', command = self.Upload_photo)
        self.Upload.place(x = 200, y = 520, width = 200)
        

        self.Add_data = ttk.Button(self.f3, text = 'ADD', command = self.AddData)
        self.Add_data.place(x = 10, y =570, width = 100, height = 40)


        self.Update = ttk.Button(self.f3, text = 'UPDATE', command = self.UpdData)
        self.Update.place(x = 160, y =570, width = 120, height = 40)

        self.Delete_data = ttk.Button(self.f3, text = 'DELETE', command = self.delete_da)
        self.Delete_data.place(x = 330, y =570, width = 120, height = 40)

        self.Clear = ttk.Button(self.f3, text = 'CLEAR', command = self.Clear_)
        self.Clear.place(x = 495, y = 570, width = 100, height = 40)







    def only_numeric_input(self,P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
        if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
            return True
        elif keyboard.is_pressed('space'):
            return True

        return False
        
    def only_string_input(self,P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
        if P.isalpha() or P == '':
            return True
        elif keyboard.is_pressed('space'):
            return True
        elif keyboard.is_pressed('backspace'):
            return True
        
        alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for i in alph:
            if keyboard.is_pressed(i):
                return True
            elif keyboard.is_pressed(i.upper()):
                return True

        else:
            return False


    def only_numeric_input_phone(self,P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
        if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
            return True
        return False
        




    def Upload_photo(self):

        self.profile_photo = tk.filedialog.askopenfilename(title = 'student Photo', filetypes = (("png files", "*.png"), ("jpg files", "*.jpg"),("all files", "*.*")) )

        self.output = io.BytesIO()

        self.a = Image.open(str(self.profile_photo))
        self.b = self.a.resize((138,190))
        self.b.save(self.output, format = 'PNG')
        
        self.binaryData = self.output.getvalue()
        return self.binaryData

    def AddData(self):

        import re

        self.regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        import phonenumbers

        my_string_number = self.ph_cc.get() + self.ph_ent.get()
        print(my_string_number)
        my_number = phonenumbers.parse(my_string_number)

        ph = phonenumbers.is_possible_number(my_number)


        E_mail_validate = False
        phone_number_validate = False

        if(re.search(self.regex, self.E_mail_ent.get())):
            E_mail_validate = True
 
        else:
            E_mail_validate = False
            tk.messagebox.showinfo('E-mail', 'Invalid E-mail')

        if ph == True:
            phone_number_validate = True
        
        else:
            phone_number_validate = False
            tk.messagebox.showinfo('Phone Number', 'Invalid Phone Number')


        if E_mail_validate == True and phone_number_validate == True:


            query1 = f"Insert into school_management.student_table(student_id, Student_name, Class, Gender) values( {self.stu_id_ent.get()}, '{self.Name_ent.get()}', '{self.Class_ent.get()}', '{self.Gender_ent.get()}')"

            query2 = f"Insert into school_management.student_details(student_id, student_name, father_name, mother_name, date_of_birth) values( {self.stu_id_ent.get()}, '{self.Name_ent.get()}', '{self.Fath_ent.get()}', '{self.mother_ent.get()}', '{self.Date.get()}')"

            self.phoneNumber = str(self.ph_cc.get()) + str(self.ph_ent.get())


            query3 = f"Insert into school_management.contact_table(student_id, phone_no, e_mail) values({self.stu_id_ent.get()}, '{self.phoneNumber}', '{self.E_mail_ent.get()}')"

            query4 = f"Insert into school_management.address_table(student_id, Address) values({self.stu_id_ent.get()}, '{self.Adress_ent.get(1.0, tk.END)}')"

            query5 = f"Insert into school_management.student_profile values(%s, %s)"
            insert_photo = (self.stu_id_ent.get(), self.binaryData)



            try:
                self.cur.execute(query1)
                self.cur.execute(query2)
                self.cur.execute(query3)
                self.cur.execute(query4)
                self.cur.execute(query5, insert_photo)

            except mysql.connector.IntegrityError as e:

                print(format(e))
            
            


            
            self.conn.commit()

            for record in self.student_list.get_children():
                self.student_list.delete(record)
            
            self.cur.execute('SELECT ROW_NUMBER() Over (Order by student_table.student_id) AS SN, student_table.student_id, student_table.Student_name, student_table.Class ,student_table.Gender,  student_details.date_of_birth ,student_details.father_name, student_details.mother_name,contact_table.phone_no, contact_table.e_mail, address_table.address, student_profile.profile_photo from ((((student_table inner join student_details on student_table.student_id = student_details.student_id) inner join contact_table on student_table.student_id = contact_table.student_id) inner join address_table on student_table.student_id = address_table.student_id) inner join student_profile on student_table.student_id = student_profile.student_id);')

            rows = self.cur.fetchall()

            self.count = 0

            for row in rows:
                self.student_list.insert(parent='', index='end',iid = self.count, text='Parent', values=(row))

                self.count += 1



        


        
    def UpdData(self):

        import re

        self.regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        import phonenumbers

        my_string_number = self.ph_cc.get() + self.ph_ent.get()
        print(my_string_number)
        my_number = phonenumbers.parse(my_string_number)

        ph = phonenumbers.is_possible_number(my_number)


        E_mail_validate = False
        phone_number_validate = False

        if(re.search(self.regex, self.E_mail_ent.get())):
            E_mail_validate = True
 
        else:
            E_mail_validate = False
            tk.messagebox.showinfo('E-mail', 'Invalid E-mail')

        if ph == True:
            phone_number_validate = True
        
        else:
            phone_number_validate = False
            tk.messagebox.showinfo('Phone Number', 'Invalid Phone Number')


        if E_mail_validate == True and phone_number_validate == True:



            query1 = f"Update school_management.student_table set student_name = '{self.Name_ent.get()}', Class = '{self.Class_ent.get()}' , Gender = '{self.Gender_ent.get()} ' where  student_id = {self.stu_id_ent.get()}"

            query2 = f"Update school_management.student_details set student_name = '{self.Name_ent.get()}', father_name = '{self.Fath_ent.get()}', mother_name = '{self.mother_ent.get()}' ,date_of_birth = '{self.Date.get()}', Gender = '{self.Gender_ent.get()}' where  student_id = {self.stu_id_ent.get()}"

            self.phoneNumber = str(self.ph_cc.get()) + str(self.ph_ent.get())


            query3 = f"Update school_management.contact_table set phone_no = '{self.phoneNumber}', e_mail = '{self.E_mail_ent.get()}' where student_id = {self.stu_id_ent.get()} "

            query4 = f"Update school_management.address_table set Address = '{self.Adress_ent.get(1.0, tk.END)}' where student_id = {self.stu_id_ent.get()}"

            query = f"Update school_management.student_profile set profile_photo = %s where student_id = %s"
            values_quer = (self.binaryData, self.stu_id_ent.get())
            query5 = (query, values_quer)
            print(query5)
            



            self.cur.execute(query1)
            self.cur.execute(query2)
            self.cur.execute(query3)
            self.cur.execute(query4)
            self.cur.execute(query, values_quer)


            self.conn.commit()


            for record in self.student_list.get_children():
                self.student_list.delete(record)
            
            self.cur.execute('SELECT ROW_NUMBER() Over (Order by student_table.student_id) AS SN, student_table.student_id, student_table.Student_name, student_table.Class ,student_table.Gender,  student_details.date_of_birth ,student_details.father_name, student_details.mother_name,contact_table.phone_no, contact_table.e_mail, address_table.address, student_profile.profile_photo from ((((student_table inner join student_details on student_table.student_id = student_details.student_id) inner join contact_table on student_table.student_id = contact_table.student_id) inner join address_table on student_table.student_id = address_table.student_id) inner join student_profile on student_table.student_id = student_profile.student_id);')

            rows = self.cur.fetchall()

            self.count = 0

            for row in rows:
                self.student_list.insert(parent='', index='end',iid = self.count, text='Parent', values=(row))

                self.count += 1





    def delete_da(self):
        query1 = f"Delete from school_management.student_table where student_id = {self.stu_id_ent.get()} "
        query2 = f"Delete from school_management.student_profile where student_id = {self.stu_id_ent.get()}"
        query3 = f"Delete from school_management.student_details where student_id = {self.stu_id_ent.get()}"
        query4 = f"Delete from school_management.address_table where student_id = {self.stu_id_ent.get()}"
        query5 = f"Delete from school_management.contact_table where student_id = {self.stu_id_ent.get()}"

        
        
        self.cur.execute(query2)
        self.cur.execute(query3)
        self.cur.execute(query4)
        self.cur.execute(query5)
        self.cur.execute(query1)

        self.conn.commit()

        for record in self.student_list.get_children():
            self.student_list.delete(record)
        
        self.cur.execute('SELECT ROW_NUMBER() Over (Order by student_table.student_id) AS SN, student_table.student_id, student_table.Student_name, student_table.Class ,student_table.Gender,  student_details.date_of_birth ,student_details.father_name, student_details.mother_name,contact_table.phone_no, contact_table.e_mail, address_table.address, student_profile.profile_photo from ((((student_table inner join student_details on student_table.student_id = student_details.student_id) inner join contact_table on student_table.student_id = contact_table.student_id) inner join address_table on student_table.student_id = address_table.student_id) inner join student_profile on student_table.student_id = student_profile.student_id);')

        rows = self.cur.fetchall()

        self.count = 0

        for row in rows:
            self.student_list.insert(parent='', index='end',iid = self.count, text='Parent', values=(row))

            self.count += 1


    
    def Clear_(self):
        self.Name_ent.delete('0', tk.END)
        self.stu_id_ent.delete('0', tk.END)
        self.Gender_ent.set('')
        timing = datetime.now()
        todays_date = timing.strftime("%m/%d/%y")
        self.Date.set_date(todays_date)

        self.Fath_ent.delete(0, tk.END)
        self.mother_ent.delete(0, tk.END)
        self.ph_cc.set('')
        self.ph_ent.delete(0, tk.END)

        self.Adress_ent.delete(1.0, tk.END)
        self.E_mail_ent.delete(0, tk.END)
        self.Class_ent.set('')
        


        for record in self.student_list.get_children():
            self.student_list.delete(record)
        
        self.cur.execute('SELECT ROW_NUMBER() Over (Order by student_table.student_id) AS SN, student_table.student_id, student_table.Student_name, student_table.Class ,student_table.Gender,  student_details.date_of_birth ,student_details.father_name, student_details.mother_name,contact_table.phone_no, contact_table.e_mail, address_table.address, student_profile.profile_photo from ((((student_table inner join student_details on student_table.student_id = student_details.student_id) inner join contact_table on student_table.student_id = contact_table.student_id) inner join address_table on student_table.student_id = address_table.student_id) inner join student_profile on student_table.student_id = student_profile.student_id);')

        rows = self.cur.fetchall()

        self.count = 0

        for row in rows:
            self.student_list.insert(parent='', index='end',iid = self.count, text='Parent', values=(row))

            self.count += 1
