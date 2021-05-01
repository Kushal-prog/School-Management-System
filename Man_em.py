import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import datetime
import keyboard
import mysql.connector
from tkinter import filedialog
import io
import pymysql
from PIL import Image, ImageTk
from datetime import datetime
import re





class Man_em1():

    def __init__(self, frame_name):

        self.frame_name = frame_name

        self.style = ttk.Style()

        self.note1 = ttk.Notebook(self.frame_name)

        self.Edit_de = tk.Frame(self.frame_name, height = 700, width = 1350, bg = 'black')
        self.Edit_de.config()

        self.Users = tk.Frame(self.frame_name, height = 720, width = 1350, bg = 'black')


        self.note1.add(self.Edit_de, text = '                                   EDIT                                       ')
        self.note1.add(self.Users, text = '                                          Accounts                                              ')


        self.note1.place(x = 0, y = 45)

        #call the employee label function
        self.Emplo_lab()

        #call the employee Entry function
        self.Employee_Ent()

        #call the employee list function
        self.Employee_list_func()

        #call the employee Buttons function
        self.Employee_Buttons()


        self.conn = mysql.connector.connect(host = 'localhost', database = 'school_management', user = 'root', password = 'Kushal@2006',charset='utf8',auth_plugin='mysql_native_password' )

        self.cur = self.conn.cursor()



# function for employee label
    def Emplo_lab(self):


        self.Name_lab = tk.Label(self.Edit_de, text = 'Name:', font = 'Arial 20', bg = 'black', fg= 'white')
        self.Name_lab.place(x = 5, y = 30)

        
        
        self.emp_id_lab = tk.Label(self.Edit_de, text = 'ID:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.emp_id_lab.place(x = 5, y = 100)

        
 
        self.Job_lab = tk.Label(self.Edit_de, text = 'Job:', font = 'Arial 20',bg = 'black', fg = 'white')
        self.Job_lab.place(x = 5, y = 170)


        self.Gender_lab = tk.Label(self.Edit_de, text = 'Gender:', font = 'Arial 20', bg = 'black', fg = 'white')

        self.Gender_lab.place(x = 5, y = 310)

        
        self.Date_lab = tk.Label(self.Edit_de, text = 'D.O.B:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.Date_lab.place(x = 5, y = 240)

        self.phone_no = tk.Label(self.Edit_de, text = 'Phone No:', font = 'Arial 20', bg = 'black', fg = 'white')

        self.phone_no.place(x = 375, y = 30)

        

        self.E_mail_lab = tk.Label(self.Edit_de, text = 'E-Mail:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.E_mail_lab.place(x = 375, y = 100)

        

        self.Fath_lab = tk.Label(self.Edit_de, text = 'Father Name:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.Fath_lab.place(x = 375 , y = 170)

        

        self.Adress_lab = tk.Label(self.Edit_de, text = 'Address: ', font = 'Arial 20', bg = 'black', fg = 'white')
        self.Adress_lab.place(x = 375, y = 240)

        self.Upload_lab = tk.Label(self.Edit_de, text = 'Upload Photo:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.Upload_lab.place(x = 200, y = 410)

        #Users Tab
        self.Employee_label_Accounts = tk.Label(self.Users, text = 'Employee ID:', font = 'Arial 20', bg = 'black', fg = 'White')
        self.Employee_label_Accounts.place(x = 80, y = 10)

        self.Employee_UserName_label_Accounts = tk.Label(self.Users, text = 'Username:', font = 'Arial 20', bg = 'black', fg = 'White')
        self.Employee_UserName_label_Accounts.place(x = 110, y = 80)

        self.Employee_Password_label_Accounts = tk.Label(self.Users, text = 'Password:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.Employee_Password_label_Accounts.place(x = 118, y = 150)

        self.Employee_Confirm_Password_Accounts = tk.Label(self.Users, text = 'Confirm Password:', font = 'Arial 20', bg = 'black', fg = 'White')
        self.Employee_Confirm_Password_Accounts.place(x = 20, y = 230)

        
# function for employee Entry, combox

    def Employee_Ent(self):

        self.Name_ent = ttk.Entry(self.Edit_de, font= 'Arial 20 ')
        self.callback1 = self.Edit_de.register(self.only_string_input)
        self.Name_ent.configure(validate = "key", validatecommand =(self.callback1, "%P"))

        self.Name_ent.place(x = 110, y = 30, height = 35, width = 250)



        self.emp_id_ent = ttk.Entry(self.Edit_de, font= 'Arial 20 ')
        self.callback = self.Edit_de.register(self.only_numeric_input)
        self.emp_id_ent.configure(validate = "key", validatecommand =(self.callback, "%P"))

        self.emp_id_ent.place(x = 110, y = 100, height = 35, width = 250)


        
        self.select_Job = tk.StringVar()

        self.Job_ent = ttk.Combobox(self.Edit_de, font= 'Arial 20 ', textvariable = self.select_Job, state ='readonly')

        self.Job_ent['values'] = ('principle','teacher')

        self.Job_ent.place(x = 110, y = 170, width = 250)



        select_Gender = tk.StringVar()
        self.Gender_ent = ttk.Combobox(self.Edit_de, font = 'Arial 20', textvariable = select_Gender, state ='readonly')        
        self.Gender_ent['values'] = ('Male', 'Female', 'Other')
        self.Gender_ent.place(x = 110, y = 310, width = 250)



        self.Date = DateEntry(self.Edit_de,width=20,background="darkblue",fg="white",year=2021,font = 'Arial 20', state = 'readonly')
        self.Date.place(x = 110, y = 240, width = 250)



        select_cc = tk.IntVar()
        self.ph_cc = ttk.Combobox(self.Edit_de, font = 'Arial 20', textvariable = select_cc, values = ('+91','+62'), state ='readonly')

        self.ph_cc.place(x = 545, y = 30, width = 70)

        self.ph_ent = ttk.Entry(self.Edit_de, font= 'Arial 20 ')

        self.callback2 = self.callback = self.Edit_de.register(self.only_numeric_input_phone)

        self.ph_ent.configure(validate = "key", validatecommand =(self.callback2, "%P"))

        self.ph_ent.place(x = 615, y = 30, width = 180)

        self.E_mail_ent = tk.Entry(self.Edit_de, font = 'Arial 17')
        self.E_mail_ent.place(x = 545, y = 100, width = 250)



        self.Fath_ent = ttk.Entry(self.Edit_de, font= 'Arial 20')
        self.Fath_ent.place(x = 545, y = 170, width = 250)



        self.Adress_ent = tk.Text(self.Edit_de ,font = 'Arial 15')
        self.Adress_ent.place(x = 545, y = 240, height = 110, width = 250)


        #Accounts

        self.Employee_Ent_Accounts = tk.Entry(self.Users, font= 'Arial 20')
        self.Employee_Ent_Accounts.place(x = 250, y = 10)

        self.callback2 = self.callback = self.Users.register(self.only_numeric_input)
        self.Employee_Ent_Accounts.configure(validate = "key", validatecommand =(self.callback2, "%P"))

        self.Employee_Ent_Username = tk.Entry(self.Users, font= 'Arial 20')
        self.Employee_Ent_Username.place(x = 250, y = 80)

        self.Employee_Ent_Password = tk.Entry(self.Users, font= 'Arial 20')
        self.Employee_Ent_Password.place(x = 250, y = 150)

        self.Employee_Ent_Con_Password = tk.Entry(self.Users, font= 'Arial 20')
        self.Employee_Ent_Con_Password.place(x = 250, y = 230)




# function for employee list
    def Employee_list_func(self):

        self.conn = mysql.connector.connect(host = 'localhost', database = 'school_management', user = 'root', password = 'Kushal@2006',charset='utf8',auth_plugin='mysql_native_password' )

        self.cur = self.conn.cursor()

        self.sep_er = ttk.Separator(self.Edit_de, orient = 'vertical')
        self.sep_er.place(x = 800, y = 0, height = 700)
        
        self.employee_list = ttk.Treeview(self.Edit_de)
        self.st_sc_v = ttk.Scrollbar(self.employee_list,orient = 'vertical', command = self.employee_list.yview)
        self.st_sc_h = ttk.Scrollbar(self.employee_list,orient = 'horizontal', command = self.employee_list.xview)

        self.employee_list.configure(yscrollcommand = self.st_sc_v.set)
        self.employee_list.configure(xscrollcommand = self.st_sc_h.set)

        self.employee_list.place(x = 810, y = 100, width = 525, height = 500)
        self.st_sc_v.pack(side = tk.RIGHT, fill = tk.Y)
        self.st_sc_h.pack(side = tk.BOTTOM, fill = tk.X)

        
        self.employee_list['column'] = ('Sn','Employee ID','Name', 'Job', 'Gender', 'D.O.B', 'Father Name','Phone No', 'E-mail','Address', 'Photo', 'Face ID')

        self.employee_list.column('#0', width=0,stretch=tk.NO)
        self.employee_list.column('Sn', width = 100)
        
        self.employee_list.column('Employee ID',anchor=tk.CENTER ,width=80)

        self.employee_list.column('Name',anchor=tk.W ,width=120)
        self.employee_list.column('Job', anchor=tk.W,width=80)
        self.employee_list.column('E-mail', anchor=tk.W,width=80)
        self.employee_list.column('Gender', anchor=tk.W,width=80)
        self.employee_list.column('D.O.B', anchor = tk.W, width=80)
        self.employee_list.column('Father Name', anchor = tk.W, width=80)
        self.employee_list.column('Phone No', anchor = tk.W, width=80)
        
        self.employee_list.column('Address', anchor = tk.W, width=80)
        self.employee_list.column('Photo', anchor = tk.W, width=80)
        self.employee_list.column('Face ID', anchor = tk.W, width=80)



        self.employee_list.heading('#0',text='', anchor= tk.W)
        self.employee_list.heading('Sn', text = 'Sn', anchor=tk.W)

        self.employee_list.heading('Employee ID',text='Employee ID', anchor=tk.W)

        self.employee_list.heading('Name', text='Name', anchor=tk.CENTER)

        self.employee_list.heading('Job',text='Job', anchor=tk.W)
        self.employee_list.heading('E-mail',text='E-mail', anchor=tk.W)

        self.employee_list.heading('Gender',text='Gender', anchor=tk.W)

        self.employee_list.heading('D.O.B', text = 'Date of Birth', anchor = tk.W)
        self.employee_list.heading('Father Name', text = 'Father Name', anchor=tk.W)

        self.employee_list.heading('Phone No', text = 'Phone No', anchor = tk.W)

        self.employee_list.heading('Address', text='Address', anchor=tk.W)

        self.employee_list.heading('Photo', text='Photo', anchor=tk.W)
        self.employee_list.heading('Face ID', text = 'Face ID', anchor = tk.W)


        self.cur.execute('select ROW_NUMBER() Over (Order by employee_table.employee_id) AS SN,employee_table.employee_id, employee_table.Employee_Name, job_tabel.Job, employee_table.Gender,employee_table.Date_of_birth,employee_details.Father_name, employee_contact.Phone_number,employee_contact.E_mail,employee_address.address, employee_profile.employee_photo from (((((employee_table inner join employee_address on  employee_address.employee_id = employee_table.employee_id) inner join employee_details on  employee_details.employee_id = employee_table.employee_id) inner join employee_contact on  employee_contact.employee_id = employee_table.employee_id) inner join job_tabel on job_tabel.employee_id = employee_table.employee_id) inner join employee_profile on employee_profile.employee_id = employee_table.employee_id) order by employee_table.employee_id asc;')

        rows = self.cur.fetchall()

        self.count = 0

        for row in rows:
            self.employee_list.insert(parent='', index='end',iid=self.count, text='Parent', values=(row))

            self.count += 1



        self.style.configure('TButton', font = 'Arial 20', foreground  = 'red', background = 'blue', borderwidth = 10)
        self.style.map('TButton', foreground = [('active', 'red'), ('pressed', 'red')])

        self.Search_d_lab = tk.Label(self.Edit_de, text = 'Search By:', font = 'Arial 20', bg = 'black', fg = 'white')
        self.Search_d_lab.place(x = 810, y= 10)

        search_value = tk.StringVar()

        self.Search_d_combo = ttk.Combobox(self.Edit_de, font = 'Arial 20', textvariable = search_value, state = 'readonly')
        
        self.Search_d_combo['values'] = (
            'Name',
            'Emp ID', 
            'E-mail',
            'Phone No'
            )

        self.Search_d_combo.place(x = 950, y= 10, width = 150)

        self.search_ent = ttk.Entry(self.Edit_de, font= 'Arial 20')
        self.search_ent.place(x = 1100, y = 10, width = 140)

        self.search_but = ttk.Button(self.Edit_de, text = 'Search')
        self.search_but.place(x = 1250, y = 10, width = 95)

        self.showall = ttk.Button(self.Edit_de, text = 'Show All')
        self.showall.place(x = 810, y = 55, height = 40)

        self.employee_list.bind('<ButtonRelease - 1>', self.selected_item)





        self.employee_account_list = ttk.Treeview(self.Users)
        self.st_sc_v1 = ttk.Scrollbar(self.employee_account_list,orient = 'vertical', command = self.employee_account_list.yview)
        self.st_sc_h1 = ttk.Scrollbar(self.employee_account_list,orient = 'horizontal', command = self.employee_account_list.xview)

        self.employee_account_list.configure(yscrollcommand = self.st_sc_v1.set)
        self.employee_account_list.configure(xscrollcommand = self.st_sc_h1.set)

        self.employee_account_list.place(x = 610, y = 0, width = 625, height = 600)
        self.st_sc_v1.pack(side = tk.RIGHT, fill = tk.Y)
        self.st_sc_h1.pack(side = tk.BOTTOM, fill = tk.X)

        
        self.employee_account_list['column'] = ('Sn','Employee ID','Name', 'Username', 'Password', 'Face ID')

        self.employee_account_list.column('#0', width=0,stretch=tk.NO)
        self.employee_account_list.column('Sn', width = 100)
        self.employee_account_list.column('Employee ID',anchor=tk.CENTER ,width=80)
        self.employee_account_list.column('Name',anchor=tk.W ,width=120)
        self.employee_account_list.column('Username', anchor=tk.W,width=80)
        self.employee_account_list.column('Password', anchor=tk.W,width=80)
        self.employee_account_list.column('Face ID', anchor = tk.W, width=80)

        self.employee_account_list.heading('#0',text='', anchor= tk.W)
        self.employee_account_list.heading('Sn', text = 'Sn', anchor=tk.W)

        self.employee_account_list.heading('Employee ID',text='Employee ID', anchor=tk.W)

        self.employee_account_list.heading('Name', text='Name', anchor=tk.CENTER)

        self.employee_account_list.heading('Username',text='Job', anchor=tk.W)
        self.employee_account_list.heading('Password',text='E-mail', anchor=tk.W)

        self.employee_account_list.heading('Face ID', text = 'Face ID', anchor = tk.W)


        self.cur.execute('select ROW_NUMBER() Over (Order by employee_table.employee_id) AS SN, employee_table.Employee_name, employee_acount_login.Username, employee_acount_login.Password from employee_table inner join employee_acount_login on employee_table.employee_id = employee_acount_login.employee_id')

        rows1 = self.cur.fetchall()

        self.count1 = 0

        for row1 in rows1:
            self.employee_account_list.insert(parent='', index='end',iid=self.count, text='Parent', values=(row))
            self.count += 1


    def selected_item(self, event):

        self.Name_ent.delete(0, tk.END)
        self.emp_id_ent.delete(0, tk.END)
        self.Job_ent.set('')
        self.Gender_ent.set('')

        ab = datetime.now()

        date_now = ab.strftime("%x")


        self.Date.set_date(date_now)

        self.ph_cc.set('')
        self.ph_ent.delete(0, tk.END)

        self.E_mail_ent.delete(0, tk.END)
        self.Fath_ent.delete(0, tk.END)
        self.Adress_ent.delete(1.0, tk.END)

        selected = self.employee_list.focus()
        values_employee_list = self.employee_list.item(selected, 'values')
        #print(values_employee_list)

        self.Name_ent.insert(0, values_employee_list[2])
        self.emp_id_ent.insert(0, values_employee_list[1])
        self.Job_ent.set(values_employee_list[3])
        self.Gender_ent.set(values_employee_list[4])
        Phone_number_list = []

        for Phone_number_ in values_employee_list[7]:
            Phone_number_list.append(Phone_number_)

        Phone_number_code = Phone_number_list[0] + Phone_number_list[1] + Phone_number_list[2]
        a = Phone_number_list[3: len(Phone_number_list) + 1]
        a = "".join(a)

        self.ph_cc.set(Phone_number_code)
        self.ph_ent.insert(0, a)

        self.E_mail_ent.insert(0, values_employee_list[8])
        self.Fath_ent.insert(0, values_employee_list[6])
        self.Adress_ent.insert(1.0, values_employee_list[9])

        self.binaryData = values_employee_list[10]








        






# function for employee Buttons
    def Employee_Buttons(self):

        self.style.configure('TButton', font = 'Arial 20', foreground  = 'red', background = 'blue', borderwidth = 10)
        self.style.map('TButton', foreground = [('active', 'red'), ('pressed', 'red')])

        self.Upload = ttk.Button(self.Edit_de, text = 'Select Photo', command = self.upload_photo)
        self.Upload.place(x = 400, y = 410, width = 200)
        
        self.Add_data = ttk.Button(self.Edit_de, text = 'ADD', command = self.AddData)
        self.Add_data.place(x = 30, y = 520, width = 150, height = 40)

        self.Update = ttk.Button(self.Edit_de, text = 'UPDATE', command = self.Update_data)
        self.Update.place(x = 200, y =520, width = 150, height = 40)

        self.Delete_data = ttk.Button(self.Edit_de, text = 'DELETE', command = self.delete_data_func)
        self.Delete_data.place(x = 400, y =520, width = 150, height = 40)

        self.Clear = ttk.Button(self.Edit_de, text = 'CLEAR',command = self.Clear_func)
        self.Clear.place(x = 600, y = 520, width = 150, height = 40)

        self.Acc_User = ttk.Button(self.Users, text = 'Add Account')
        self.Acc_User.place(x = 40, y = 500, width = 200, height = 40)

        self.Update_User = ttk.Button(self.Users, text = 'Update Account')
        self.Update_User.place(x = 300, y = 500, width = 210, height = 40)


    # def Add_acc(self):

        # self.cur.execute(f"Insert into employee_account_login(Sn, Username, Password) values({self.}')")


    
    def upload_photo(self):

        self.upload_em_pho = tk.filedialog.askopenfilename(title = 'student Photo', filetypes = (("png files", "*.png"), ("jpg files", "*.jpg"),("all files", "*.*")))

        self.output = io.BytesIO()

        self.a = Image.open(str(self.upload_em_pho))
        self.b = self.a.resize((180,240))
        self.b.save(self.output, format = 'PNG')
        
        self.binaryData = self.output.getvalue()
        return self.binaryData



    


    


    def only_numeric_input(self,P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
        if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
            return True
        elif keyboard.is_pressed('space'):
            return True
        elif keyboard.is_pressed('backspace'):
            return True
        else:
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



        



    def AddData(self):

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


            self.conn = mysql.connector.connect(host = 'localhost', database = 'school_management', user = 'root', password = 'Kushal@2006',charset='utf8',auth_plugin='mysql_native_password' )

            self.cur = self.conn.cursor()


            query1 = f"Insert into employee_table (employee_id, Employee_Name, Gender, Date_of_birth) values ({self.emp_id_ent.get()}, '{self.Name_ent.get()}', '{self.Gender_ent.get()}', '{self.Date.get()}')"

            query2 = f"Insert into employee_details (employee_id, Employee_Name, Father_name) values ({self.emp_id_ent.get()}, '{self.Name_ent.get()}', '{self.Fath_ent.get()}')"

            query3 = f"Insert into employee_contact (employee_id, Employee_Name, Phone_number, E_mail) values({self.emp_id_ent.get()}, '{self.Name_ent.get()}', '{self.ph_cc.get() + self.ph_ent.get()}', '{self.E_mail_ent.get()}')"

            query4 = f"Insert into job_tabel (employee_id, Employee_Name, Job) values({self.emp_id_ent.get()}, '{self.Name_ent.get()}', '{self.Job_ent.get()}')"

            query5 = f"Insert into employee_address (employee_id, Employee_Name, address) values({self.emp_id_ent.get()}, '{self.Name_ent.get()}', '{self.Adress_ent.get(1.0, tk.END)}')"

            query6 = f"Insert into employee_profile (employee_id, employee_photo) values(%s, %s)"

            insert_photo = (self.emp_id_ent.get(),self.binaryData)

            self.cur.execute(query1)
            self.cur.execute(query2)
            self.cur.execute(query3)
            self.cur.execute(query4)
            self.cur.execute(query5)
            self.cur.execute(query6, insert_photo)

            self.conn.commit()




            for record in self.employee_list.get_children():
                self.employee_list.delete(record)

            self.cur.execute('select ROW_NUMBER() Over (Order by employee_table.employee_id) AS SN,employee_table.employee_id, employee_table.Employee_Name, job_tabel.Job, employee_table.Gender,employee_table.Date_of_birth,employee_details.Father_name, employee_contact.Phone_number,employee_contact.E_mail,employee_address.address, employee_profile.employee_photo from (((((employee_table inner join employee_address on  employee_address.employee_id = employee_table.employee_id) inner join employee_details on  employee_details.employee_id = employee_table.employee_id) inner join employee_contact on  employee_contact.employee_id = employee_table.employee_id) inner join job_tabel on job_tabel.employee_id = employee_table.employee_id) inner join employee_profile on employee_profile.employee_id = employee_table.employee_id) order by employee_table.employee_id asc;')


            rows = self.cur.fetchall()

            self.count = 0

            for row in rows:
                self.employee_list.insert(parent='', index='end',iid=self.count, text='Parent', values=(row))

                self.count += 1



            self.style.configure('TButton', font = 'Arial 20', foreground  = 'red', background = 'blue', borderwidth = 10)
            self.style.map('TButton', foreground = [('active', 'red'), ('pressed', 'red')])


    
    def Update_data(self):


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

            query1 = f"Update employee_table set Employee_Name = '{self.Name_ent.get()}', Gender = '{self.Gender_ent.get()}', Date_of_birth = '{self.Date.get()}' where employee_id = {self.emp_id_ent.get()}"

            query2 = f"Update employee_details set Employee_Name = '{self.Name_ent.get()}', Father_name = '{self.Fath_ent.get()}' where employee_id =  {self.emp_id_ent.get()}"

            query3 = f"Update employee_contact set Employee_Name = '{self.Name_ent.get()}', Phone_number = '{self.ph_cc.get() + self.ph_ent.get()}' , E_mail = '{self.E_mail_ent.get()}' where employee_id =  {self.emp_id_ent.get()}"

            query4 = f"Update employee_address set Employee_Name = '{self.Name_ent.get()}', address = '{self.Adress_ent.get(1.0, tk.END)}' where employee_id = {self.emp_id_ent.get()}"

            query5 = f"Update employee_profile set employee_photo = %s where employee_id = %s"
            values_quer = (self.binaryData, self.emp_id_ent.get())

            query6 = f"Update job_tabel set Employee_Name = '{self.Name_ent.get()}', Job = '{self.Job_ent.get()}' where employee_id =  {self.emp_id_ent.get()}"


            self.cur.execute(query1)
            self.cur.execute(query2)
            self.cur.execute(query3)
            self.cur.execute(query4)
            self.cur.execute(query5, values_quer)
            self.cur.execute(query6)


            self.conn.commit()

            for record in self.employee_list.get_children():
                self.employee_list.delete(record)

            self.cur.execute('select ROW_NUMBER() Over (Order by employee_table.employee_id) AS SN,employee_table.employee_id, employee_table.Employee_Name, job_tabel.Job, employee_table.Gender,employee_table.Date_of_birth,employee_details.Father_name, employee_contact.Phone_number,employee_contact.E_mail,employee_address.address, employee_profile.employee_photo from (((((employee_table inner join employee_address on  employee_address.employee_id = employee_table.employee_id) inner join employee_details on  employee_details.employee_id = employee_table.employee_id) inner join employee_contact on  employee_contact.employee_id = employee_table.employee_id) inner join job_tabel on job_tabel.employee_id = employee_table.employee_id) inner join employee_profile on employee_profile.employee_id = employee_table.employee_id) order by employee_table.employee_id asc;')


            rows = self.cur.fetchall()

            self.count = 0

            for row in rows:
                self.employee_list.insert(parent='', index='end',iid=self.count, text='Parent', values=(row))

                self.count += 1

    def delete_data_func(self):

        query1 = f"delete from employee_profile where employee_id = {self.emp_id_ent.get()} "
        query2 = f"delete from employee_details where employee_id = {self.emp_id_ent.get()} "
        query3 = f"delete from employee_contact where employee_id = {self.emp_id_ent.get()} "
        query4 = f"delete from employee_address where employee_id = {self.emp_id_ent.get()} "
        query5 = f"delete from job_tabel where employee_id = {self.emp_id_ent.get()}"
        query6 = f"delete from employee_table where employee_id = {self.emp_id_ent.get()} "

        self.cur.execute(query1)
        self.cur.execute(query2)
        self.cur.execute(query3)
        self.cur.execute(query4)
        self.cur.execute(query5)
        self.cur.execute(query6)

        self.conn.commit()

        for record in self.employee_list.get_children():
            self.employee_list.delete(record)

        self.cur.execute('select ROW_NUMBER() Over (Order by employee_table.employee_id) AS SN,employee_table.employee_id, employee_table.Employee_Name, job_tabel.Job, employee_table.Gender,employee_table.Date_of_birth,employee_details.Father_name, employee_contact.Phone_number,employee_contact.E_mail,employee_address.address, employee_profile.employee_photo from (((((employee_table inner join employee_address on  employee_address.employee_id = employee_table.employee_id) inner join employee_details on  employee_details.employee_id = employee_table.employee_id) inner join employee_contact on  employee_contact.employee_id = employee_table.employee_id) inner join job_tabel on job_tabel.employee_id = employee_table.employee_id) inner join employee_profile on employee_profile.employee_id = employee_table.employee_id) order by employee_table.employee_id asc;')


        rows = self.cur.fetchall()

        self.count = 0

        for row in rows:
            self.employee_list.insert(parent='', index='end',iid=self.count, text='Parent', values=(row))

            self.count += 1

    def Clear_func(self):

        self.Name_ent.delete('0', tk.END)
        self.emp_id_ent.delete('0', tk.END)
        self.Gender_ent.set('')
        timing = datetime.now()
        todays_date = timing.strftime("%m/%d/%y")
        self.Date.set_date(todays_date)

        self.Fath_ent.delete(0, tk.END)
        self.ph_cc.set('')
        self.ph_ent.delete(0, tk.END)

        self.Adress_ent.delete(1.0, tk.END)
        self.E_mail_ent.delete(0, tk.END)
        self.Job_ent.set('')