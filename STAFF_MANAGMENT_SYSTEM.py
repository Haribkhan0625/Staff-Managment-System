from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import sqlite3
from tkinter import messagebox

class login_and_registration:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("LOGIN AND REGISTRATION")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # background image
        self.bg = ImageTk.PhotoImage(file="D:\STAFF MANAGMENT SYSTEM\pattern.png")
        bg = Label(self.root, image=self.bg)
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Login or signup Frame
        Login_Frame = Frame(self.root, bg="#292929")
        Login_Frame.place(x=410, y=150, height=400, width=480)

        title = Label(Login_Frame, text="LOGIN AND SIGN UP", font=("Impact", 35, "bold"), fg="#33A1C9", bg="#292929")
        title.place(x=10, y=30)
        desc = Label(Login_Frame, text="Member Login Area", font=("Goudy old style", 15, "bold"), fg="#858585", bg="#292929")
        desc.place(x=10, y=100)

        lbl_NOTE = Label(root, text="NOTE :", font=("Goudy old style", 15, "bold"), bg="#292929",fg="#DC143C")
        lbl_NOTE.place(x=760, y=660)
        lbl_belongs_to = Label(root, text="'THIS SOFTWARE BELONGS TO ABDUL WAHAB KHAN'", font=("Goudy old style", 12, "bold"), fg="#6C7B8B", bg="#292929")
        lbl_belongs_to.place(x=840, y=660)

        lbl_user = Label(Login_Frame, text="Username", font=("Goudy old style", 15, "bold"), fg="#6C7B8B", bg="#292929")
        lbl_user.place(x=10, y=140)
        self.txt_user = Entry(Login_Frame, font=("times new roman", 15), bg="black",fg="white")
        self.txt_user.place(x=10, y=170, width=350, height=35)

        lbl_pass = Label(Login_Frame, text="Password", font=("Goudy old style", 15, "bold"), fg="#6C7B8B", bg="#292929")
        lbl_pass.place(x=10, y=210)

        self.txt_pass = Entry(Login_Frame, font=("times new roman", 15), bg="black", fg="white",show="*")
        self.txt_pass.place(x=10, y=240, width=350, height=35)

        lbl_greeting = Label(Login_Frame, text="'INICIE SESIÓN AQUÍ'", font=("Goudy old style", 15, "bold"), fg="#7D9EC0", bg="#292929")
        lbl_greeting.place(x=10, y=305)

        lbl_greeting2 = Label(Login_Frame, text="'REGÍSTRESE AQUÍ'", font=("Goudy old style", 15, "bold"), fg="#DC143C", bg="#292929")
        lbl_greeting2.place(x=15, y=355)

        Login_btn = Button(Login_Frame, text="LOGIN",command=self.login, cursor="hand2", bd=0, font=("times new roman", 20), bg="#7D9EC0", fg="black")
        Login_btn.place(x=255, y=300, width=180, height=40)

        Signup_btn = Button(Login_Frame, text="SIGN UP", command=self.signup, cursor="hand2", bd=0, font=("times new roman", 20), bg="#DC143C", fg="black")
        Signup_btn.place(x=255, y=350, width=180, height=40)



    def login(self):
     if self.txt_user.get() == "" or self.txt_pass.get() == "":
        messagebox.showerror("Error", "All fields are required!")
     else:
        con = sqlite3.connect('staff_database.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM Users WHERE username=? AND password=?", (self.txt_user.get(), self.txt_pass.get()))
            row = cur.fetchone()
            if row is not None:
                self.root.destroy()
                root = Tk() 
                obj = Staff(root) 
                root.mainloop()
            else:
                messagebox.showerror("Error", "Invalid username or password")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
        finally:
            con.close()
    
    def signup(self):
     if self.txt_user.get() == "" or self.txt_pass.get() == "":
        messagebox.showerror("Error", "All fields are required!")
     else:
        con = sqlite3.connect('staff_database.db')
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO Users (username, password) VALUES (?, ?)",
                        (self.txt_user.get(), self.txt_pass.get()))
            con.commit()
            messagebox.showinfo("Success", "Signup Successful!")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
        finally:
            con.close()


class Staff:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("STAFF MANAGEMENT SYSTEM")

        # Variables
        self.var_ID = StringVar()
        self.var_NAME = StringVar()
        self.var_DESIGNATION = StringVar()
        self.var_SHIFT = StringVar()
        self.var_HIREDATE = StringVar()
        self.var_CONTRACT = StringVar()
        self.var_CNIC = StringVar()
        self.var_GENDER = StringVar()
        self.var_DOB = StringVar()
        self.var_PHONE = StringVar()
        self.var_EMAIL = StringVar()
        self.var_ADDRESS = StringVar()
        self.var_SALARY = StringVar()
        self.var_QUALIFICATION = StringVar()
        

        self.conn = sqlite3.connect('staff_database.db')
        self.c = self.conn.cursor()

        self.create_tables()

        # title
        lbl_title = Label(text="STAFF MANAGEMENT SYSTEM", font=("arial", 50, "bold"), bg="grey", fg="black")
        lbl_title.place(x=0, y=0, width=1300, height=60)

        # main frame
        manage_frame = LabelFrame(bd=10, bg="grey", relief=RIDGE)
        manage_frame.place(x=0, y=60, width=1279, height=633)

        # left frame
        DataLeftFrame = LabelFrame(manage_frame, bd=6, relief=RIDGE, padx=2, text="STAFF DATA",
                                   font=("Arial", 20, "bold"), bg="grey", fg="red")
        DataLeftFrame.place(x=10, y=10, width=700, height=580)

        # Text
        text_label = Label(DataLeftFrame, text="(PLEASE FILL THE REQUIREMENTS)", font=("arial", 20, "bold"),
                           bg="grey", fg="black")
        text_label.place(x=0, y=0, width=620, height=120)

        # Staff Information Frame
        stf_info_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="INFORMATION : ",
                                    font=("Arial", 15, "bold"), bg="grey", fg="red")
        stf_info_frame.place(x=0, y=120, width=685, height=375)

        # Labels and Entries
        # ID
        lbl_id = Label(stf_info_frame, text="ID :", font=("arial", 12, "bold"), bg="grey")
        lbl_id.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        id_entry = ttk.Entry(stf_info_frame, textvariable=self.var_ID, width=15, font=("arial", 12, "bold"))
        id_entry.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        # Name
        lbl_Name = Label(stf_info_frame, text=" NAME :", font=("arial", 12, "bold"), bg="grey")
        lbl_Name.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        txt_name = ttk.Entry(stf_info_frame, textvariable=self.var_NAME, width=15, font=("arial", 12, "bold"))
        txt_name.grid(row=0, column=3, padx=0, pady=10, sticky=W)

        # Designation
        lbl_class = Label(stf_info_frame, text="DESIGNATION :", font=("arial", 12, "bold"), bg="grey")
        lbl_class.grid(row=2, column=0, padx=5, pady=10, sticky=W)

        combo_txt_class = ttk.Combobox(stf_info_frame, textvariable=self.var_DESIGNATION,
                                       font=("arial", 12, "bold"), width=18, state="readonly")
        combo_txt_class["value"] = ("SELECT DESIGNATION", "PROFESSOR", "ASISTANT PROFESSOR", "VISITOR", "P.A",
                                    "CLERK", "ACCOUNTANT")
        combo_txt_class.current(0)
        combo_txt_class.grid(row=2, column=1, padx=5, pady=10, sticky=W)

        # SHIFT
        lbl_roll = Label(stf_info_frame, text="SHIFT :", font=("arial", 12, "bold"), bg="grey")
        lbl_roll.grid(row=2, column=2, padx=5, pady=10, sticky=W)

        combo_txt_class = ttk.Combobox(stf_info_frame, textvariable=self.var_SHIFT, font=("arial", 12, "bold"),
                                       width=18, state="readonly")
        combo_txt_class["value"] = ("SELECT SHIFT :", "MORNING", "EVENING")
        combo_txt_class.current(0)
        combo_txt_class.grid(row=2, column=3, padx=0, pady=10, sticky=W)

        # HIRING DATE

        lbl_hiredate = Label(stf_info_frame, text="HIRE DATE :", font=("arial", 12, "bold"), bg="grey")
        lbl_hiredate.grid(row=4, column=0, padx=5, pady=10, sticky=W)

        txt_hiredate = ttk.Entry(stf_info_frame, textvariable=self.var_HIREDATE, width=15,
                                  font=("arial", 12, "bold"))
        txt_hiredate.grid(row=4, column=1, padx=5, pady=10, sticky=W)

        # CONTRACT

        lbl_contract = Label(stf_info_frame, text="CONTRACT :", font=("arial", 12, "bold"), bg="grey")
        lbl_contract.grid(row=4, column=2, padx=5, pady=10, sticky=W)

        txt_contract = ttk.Entry(stf_info_frame, textvariable=self.var_CONTRACT, width=15,
                                  font=("arial", 12, "bold"))
        txt_contract.grid(row=4, column=3, padx=0, pady=10, sticky=W)

        # CNIC

        lbl_cnic = Label(stf_info_frame, text="CNIC :", font=("arial", 12, "bold"), bg="grey")
        lbl_cnic.grid(row=6, column=0, padx=5, pady=10, sticky=W)

        txt_cnic = ttk.Entry(stf_info_frame, textvariable=self.var_CNIC, width=15,
                              font=("arial", 12, "bold"))
        txt_cnic.grid(row=6, column=1, padx=5, pady=10, sticky=W)

        # GENDER
        lbl_gender = Label(stf_info_frame, text="GENDER :", font=("arial", 12, "bold"), bg="grey")
        lbl_gender.grid(row=6, column=2, padx=5, pady=10, sticky=W)

        combo_txt_gender = ttk.Combobox(stf_info_frame, textvariable=self.var_GENDER, font=("arial", 12, "bold"),
                                         width=18, state="readonly")
        combo_txt_gender["value"] = ("SELECT GENDER :", "MALE", "FEMALE", "OTHERS")
        combo_txt_gender.current(0)
        combo_txt_gender.grid(row=6, column=3, padx=0, pady=10, sticky=W)

        # DOB
        lbl_dob = Label(stf_info_frame, text="DOB :", font=("arial", 12, "bold"), bg="grey")
        lbl_dob.grid(row=8, column=0, padx=5, pady=10, sticky=W)

        txt_dob = ttk.Entry(stf_info_frame, textvariable=self.var_DOB, width=15,
                            font=("arial", 12, "bold"))
        txt_dob.grid(row=8, column=1, padx=5, pady=10, sticky=W)

        # PHONE
        lbl_phone = Label(stf_info_frame, text="PHONE :", font=("arial", 12, "bold"), bg="grey")
        lbl_phone.grid(row=8, column=2, padx=5, pady=10, sticky=W)

        txt_phone = ttk.Entry(stf_info_frame, textvariable=self.var_PHONE, width=15,
                              font=("arial", 12, "bold"))
        txt_phone.grid(row=8, column=3, padx=0, pady=10, sticky=W)

        # EMAIL
        lbl_email = Label(stf_info_frame, text="EMAIL :", font=("arial", 12, "bold"), bg="grey")
        lbl_email.grid(row=10, column=0, padx=5, pady=10, sticky=W)

        txt_email = ttk.Entry(stf_info_frame, textvariable=self.var_EMAIL, width=15,
                              font=("arial", 12, "bold"))
        txt_email.grid(row=10, column=1, padx=5, pady=10, sticky=W)

        # ADDRESS
        lbl_address = Label(stf_info_frame, text="ADDRESS :", font=("arial", 12, "bold"), bg="grey")
        lbl_address.grid(row=10, column=2, padx=5, pady=10, sticky=W)

        txt_address = ttk.Entry(stf_info_frame, textvariable=self.var_ADDRESS, width=15,
                                font=("arial", 12, "bold"))
        txt_address.grid(row=10, column=3, padx=0, pady=10, sticky=W)

        # SALARY
        lbl_salary = Label(stf_info_frame, text="SALARY :", font=("arial", 12, "bold"), bg="grey")
        lbl_salary.grid(row=12, column=0, padx=5, pady=10, sticky=W)

        txt_salary = ttk.Entry(stf_info_frame, textvariable=self.var_SALARY, width=15,
                                font=("arial", 12, "bold"))
        txt_salary.grid(row=12, column=1, padx=5, pady=10, sticky=W)

        # QUALIFICATION
        lbl_qualification = Label(stf_info_frame, text="QUALIFICATION :", font=("arial", 12, "bold"), bg="grey")
        lbl_qualification.grid(row=12, column=2, padx=5, pady=10, sticky=W)

        combo_txt_qualification = ttk.Combobox(stf_info_frame, textvariable=self.var_QUALIFICATION,
                                               font=("arial", 12, "bold"), width=18, state="readonly")
        combo_txt_qualification["value"] = ("SELECT QUALIFICATION :", "MSc", "Mphil", "PHD", "ENGINEER", "CA",
                                            "BSc")
        combo_txt_qualification.current(0)
        combo_txt_qualification.grid(row=12, column=3, padx=0, pady=10, sticky=W)

        #button frame
        btn_frame = Frame(DataLeftFrame, bd=2, relief=RIDGE, bg="grey")
        btn_frame.place(x=0, y=500, width=680, height=38)

        btn_Add=Button(btn_frame, text="SAVE",command=self.add_data, width=16, font=("arial", 12, "bold"), bg="#7D9EC0", fg="black")
        btn_Add.grid(row=0, column=0, padx=1)

        btn_Update=Button(btn_frame, text="UPDATE",command=self.update_data, width=16, font=("arial", 12, "bold"), bg="#7D9EC0", fg="black")
        btn_Update.grid(row=0, column=1, padx=1)

        btn_Delete=Button(btn_frame, text="DELETE",command=self.delete_data, width=16, font=("arial", 12, "bold"), bg="#CD0000", fg="black")
        btn_Delete.grid(row=0, column=2, padx=1)

        btn_Reset=Button(btn_frame, text="REFRESH",command=self.clear_data, width=16, font=("arial", 12, "bold"), bg="#7D9EC0", fg="black")
        btn_Reset.grid(row=0, column=3, padx=1)


        # right frame 
        DataRightFrame = Frame(self.root, bd=6, relief=RIDGE, bg="grey")
        DataRightFrame.place(x=720, y=95, width=545, height=565)

        #search frame
        SearchFrame = Frame(DataRightFrame, bd=4, relief=RIDGE, bg="grey")
        SearchFrame.place(x=0, y=0, width=535, height=50)

        lbl_search = Label(SearchFrame, text="SEARCH BY ", font=("arial", 11, "bold"), bg="grey",width=9)
        lbl_search.grid(row=0, column=0, padx=5, pady=10, sticky=W)
        
        self.var_searchby= StringVar()

        combo_txt_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, font=("arial", 10, "bold"), width=10, state="readonly")
        combo_txt_search["value"] = ("SELECT :", "ID", "NAME", "DESIGNATION", "SALARY")
        combo_txt_search.current(0)
        combo_txt_search.grid(row=0, column=1, padx=0, pady=10, sticky=W)

        self.var_search=StringVar()

        txt_Search = ttk.Entry(SearchFrame, textvariable=self.var_search, width=9,
                              font=("arial", 12, "bold"))
        txt_Search.grid(row=0, column=4, padx=5, pady=10, sticky=W)

        btn_search=Button(SearchFrame, text="SEARCH",command=self.search_data ,width=11, font=("arial", 12, "bold"), bg="#7D9EC0", fg="black")
        btn_search.grid(row=0, column=6, padx=1)

        btn_search_all=Button(SearchFrame, text="SHOW ALL",command=self.showall ,width=11, font=("arial", 12, "bold"), bg="#7D9EC0", fg="black")
        btn_search_all.grid(row=0, column=7, padx=1)
        

        #table frame
        table_frame = LabelFrame(DataRightFrame, bd=6, relief=RIDGE, padx=2, text="STAFF DETAILS",
                                 font=("Arial", 20, "bold"), bg="grey", fg="red")
        table_frame.place(x=0, y=50, width=535, height=500)
        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.staff_table = ttk.Treeview(table_frame, column=(
            "id", "name", "designation", "shift", "hiring_date", "contract", "cnic", "gender", "dob", "phone",
            "email",
            "address", "salary", "qualification"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)

        self.staff_table.heading("id", text="ID")
        self.staff_table.heading("name", text="Name")
        self.staff_table.heading("designation", text="Designation")
        self.staff_table.heading("shift", text="Shift")
        self.staff_table.heading("hiring_date", text="Hiring Date")
        self.staff_table.heading("contract", text="Contract")
        self.staff_table.heading("cnic", text="CNIC")
        self.staff_table.heading("gender", text="Gender")
        self.staff_table.heading("dob", text="DOB")
        self.staff_table.heading("phone", text="Phone")
        self.staff_table.heading("email", text="Email")
        self.staff_table.heading("address", text="Address")
        self.staff_table.heading("salary", text="Salary")
        self.staff_table.heading("qualification", text="Qualification")

        self.staff_table['show'] = 'headings'

        self.staff_table.column("id", width=100)
        self.staff_table.column("name", width=100)
        self.staff_table.column("designation", width=100)
        self.staff_table.column("shift", width=100)
        self.staff_table.column("hiring_date", width=100)
        self.staff_table.column("contract", width=100)
        self.staff_table.column("cnic", width=100)
        self.staff_table.column("gender", width=100)
        self.staff_table.column("dob", width=100)
        self.staff_table.column("phone", width=100)
        self.staff_table.column("email", width=100)
        self.staff_table.column("address", width=100)
        self.staff_table.column("salary", width=100)
        self.staff_table.column("qualification", width=100)

        self.staff_table.pack(fill=BOTH, expand=1)

        self.staff_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

       
        

       
    def add_data(self):
        if self.var_ID.get() == "" or self.var_NAME.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            con = sqlite3.connect('sms.db')
            cur = con.cursor()
            try:
                # Insert into staff table
                cur.execute("INSERT INTO staff (ID, NAME, CNIC, GENDER, DOB) VALUES (?, ?, ?, ?, ?)",
                            (self.var_ID.get(), self.var_NAME.get(), self.var_CNIC.get(), self.var_GENDER.get(), self.var_DOB.get()))
                # Insert into contact table
                cur.execute("INSERT INTO contact (ID, PHONE, EMAIL, ADDRESS) VALUES (?, ?, ?, ?)",
                            (self.var_ID.get(), self.var_PHONE.get(), self.var_EMAIL.get(), self.var_ADDRESS.get()))
                # Insert into employment table
                cur.execute("INSERT INTO employment (ID, DESIGNATION, SHIFT, HIREDATE, CONTRACT, SALARY, QUALIFICATION) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (self.var_ID.get(), self.var_DESIGNATION.get(), self.var_SHIFT.get(), self.var_HIREDATE.get(), self.var_CONTRACT.get(), self.var_SALARY.get(), self.var_QUALIFICATION.get()))
                con.commit()
                self.fetch_data()
                self.clear_data()
                messagebox.showinfo("Success", "Record has been inserted")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}")
            finally:
                con.close()

    def fetch_data(self):
        con = sqlite3.connect('sms.db')
        cur = con.cursor()
        try:
            cur.execute("""
                SELECT staff.ID, staff.NAME, employment.DESIGNATION, employment.SHIFT, employment.HIREDATE, employment.CONTRACT,
                       staff.CNIC, staff.GENDER, staff.DOB, contact.PHONE, contact.EMAIL, contact.ADDRESS, employment.SALARY, employment.QUALIFICATION
                FROM staff
                JOIN contact ON staff.ID = contact.ID
                JOIN employment ON staff.ID = employment.ID
            """)
            rows = cur.fetchall()
            if len(rows) != 0:
                self.staff_table.delete(*self.staff_table.get_children())
                for row in rows:
                    self.staff_table.insert('', END, values=row)
                con.commit()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")
        finally:
            con.close()

    def clear_data(self):
        self.var_ID.set("")
        self.var_NAME.set("")
        self.var_DESIGNATION.set("SELECT DESIGNATION")
        self.var_SHIFT.set("SELECT SHIFT")
        self.var_HIREDATE.set("")
        self.var_CONTRACT.set("")
        self.var_CNIC.set("")
        self.var_GENDER.set("SELECT GENDER")
        self.var_DOB.set("")
        self.var_PHONE.set("")
        self.var_EMAIL.set("")
        self.var_ADDRESS.set("")
        self.var_SALARY.set("")
        self.var_QUALIFICATION.set("SELECT QUALIFICATION")

    def get_cursor(self, ev):
        cursor_row = self.staff_table.focus()
        contents = self.staff_table.item(cursor_row)
        row = contents['values']
        print("Row contents:", row)
        self.var_ID.set(row[0])
        self.var_NAME.set(row[1])
        self.var_DESIGNATION.set(row[2])
        self.var_SHIFT.set(row[3])
        self.var_HIREDATE.set(row[4])
        self.var_CONTRACT.set(row[5])
        self.var_CNIC.set(row[6])
        self.var_GENDER.set(row[7])
        self.var_DOB.set(row[8])
        self.var_PHONE.set(row[9])
        self.var_EMAIL.set(row[10])
        self.var_ADDRESS.set(row[11])
        self.var_SALARY.set(row[12])
        self.var_QUALIFICATION.set(row[13])

    def update_data(self):
        if self.var_ID.get() == "":
            messagebox.showerror("Error", "ID is required!")
        else:
            con = sqlite3.connect('sms.db')
            cur = con.cursor()
            try:
                cur.execute("""
                    UPDATE staff SET NAME=?, CNIC=?, GENDER=?, DOB=? WHERE ID=?""",
                            (self.var_NAME.get(), self.var_CNIC.get(), self.var_GENDER.get(), self.var_DOB.get(), self.var_ID.get()))
                
                cur.execute("""
                    UPDATE contact SET PHONE=?, EMAIL=?, ADDRESS=? WHERE ID=?""",
                            (self.var_PHONE.get(), self.var_EMAIL.get(), self.var_ADDRESS.get(), self.var_ID.get()))
                
                cur.execute("""
                    UPDATE employment SET DESIGNATION=?, SHIFT=?, HIREDATE=?, CONTRACT=?, SALARY=?, QUALIFICATION=? WHERE ID=?""",
                            (self.var_DESIGNATION.get(), self.var_SHIFT.get(), self.var_HIREDATE.get(), self.var_CONTRACT.get(), self.var_SALARY.get(), self.var_QUALIFICATION.get(), self.var_ID.get()))
                
                con.commit()
                self.fetch_data()
                self.clear_data()
                messagebox.showinfo("Success", "Record has been updated")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}")
            finally:
                con.close()

    def delete_data(self):
        if self.var_ID.get() == "":
            messagebox.showerror("Error", "ID is required!")
        else:
            con = sqlite3.connect('sms.db')
            cur = con.cursor()
            try:
                cur.execute("DELETE FROM staff WHERE ID=?", (self.var_ID.get(),))
                con.commit()
                self.fetch_data()
                self.clear_data()
                messagebox.showinfo("Success", "Record has been deleted")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}")
            finally:
                con.close()

    def search_data(self):
    # Get the search criteria and field to search from the comboboxes
     search_by = self.var_searchby.get()
     search_value = self.var_search.get()

     if search_by == "SELECT OPTION" or search_value == "":
        messagebox.showerror("Error", "Please select a valid search criteria and provide a search value.")
     else:
        con = sqlite3.connect('sms.db')
        cur = con.cursor()
        try:
            # Construct the query based on the selected search criteria
            if search_by == "ID":
                query = """
                    SELECT staff.ID, staff.NAME, employment.DESIGNATION, employment.SHIFT, employment.HIREDATE, employment.CONTRACT,
                           staff.CNIC, staff.GENDER, staff.DOB, contact.PHONE, contact.EMAIL, contact.ADDRESS, employment.SALARY, employment.QUALIFICATION
                    FROM staff
                    JOIN contact ON staff.ID = contact.ID
                    JOIN employment ON staff.ID = employment.ID
                    WHERE staff.ID = ?
                """
            elif search_by in ["NAME", "DESIGNATION", "SALARY"]:
                query = f"""
                    SELECT staff.ID, staff.NAME, employment.DESIGNATION, employment.SHIFT, employment.HIREDATE, employment.CONTRACT,
                           staff.CNIC, staff.GENDER, staff.DOB, contact.PHONE, contact.EMAIL, contact.ADDRESS, employment.SALARY, employment.QUALIFICATION
                    FROM staff
                    JOIN contact ON staff.ID = contact.ID
                    JOIN employment ON staff.ID = employment.ID
                    WHERE {search_by} LIKE ?
                """
            else:
                messagebox.showerror("Error", "Invalid search criteria selected.")
                return

            cur.execute(query, (search_value if search_by == "ID" else f'%{search_value}%',))
            rows = cur.fetchall()
            if len(rows) != 0:
                self.staff_table.delete(*self.staff_table.get_children())
                for row in rows:
                    self.staff_table.insert('', END, values=row)
                con.commit()
            else:
                messagebox.showinfo("Info", "No records found matching the search criteria.")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")
        finally:
            con.close()




    def showall(self):
     con = sqlite3.connect('sms.db')
     cur = con.cursor()
     try:
        cur.execute("""
            SELECT staff.ID, staff.NAME, employment.DESIGNATION, employment.SHIFT, employment.HIREDATE, employment.CONTRACT,
                   staff.CNIC, staff.GENDER, staff.DOB, contact.PHONE, contact.EMAIL, contact.ADDRESS, employment.SALARY, employment.QUALIFICATION
            FROM staff
            JOIN contact ON staff.ID = contact.ID
            JOIN employment ON staff.ID = employment.ID
        """)
        rows = cur.fetchall()
        if len(rows) != 0:
            self.staff_table.delete(*self.staff_table.get_children())
            for row in rows:
                self.staff_table.insert('', END, values=row)
     except Exception as e:
        messagebox.showerror("Error", f"Error due to: {str(e)}")
     finally:
        con.close()



    def create_tables(self):
     try:
        con = sqlite3.connect('sms.db')
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS staff (
                ID INTEGER PRIMARY KEY,
                NAME TEXT,
                CNIC TEXT,
                GENDER TEXT,
                DOB TEXT
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS contact (
                ID INTEGER PRIMARY KEY,
                PHONE TEXT,
                EMAIL TEXT,
                ADDRESS TEXT,
                FOREIGN KEY (ID) REFERENCES staff(ID)
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employment (
                ID INTEGER PRIMARY KEY,
                DESIGNATION TEXT,
                SHIFT TEXT,
                HIREDATE TEXT,
                CONTRACT TEXT,
                SALARY REAL,
                QUALIFICATION TEXT,
                FOREIGN KEY (ID) REFERENCES staff(ID)
            )
        """)
        con.commit()
     except Exception as e:
        messagebox.showerror("Error", f"Error due to: {str(e)}")
     finally:
        con.close()
    

if __name__ == "__main__":
    root = Tk()
    obj = login_and_registration(root)
    root.mainloop()

