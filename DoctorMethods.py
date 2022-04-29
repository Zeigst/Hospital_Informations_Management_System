from domains.People import *
from tkinter import *
from tkinter import ttk
from tk import *
from PIL import ImageTk, Image
import utils

def clear_entry(entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry):
    # Delete all Warnings
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                                  ', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=7,sticky='w')
    
    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    gend_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    dept_entry.delete(0, END)
    salary_entry.delete(0, END)

    # Set Selected to -1
    global selected_doctor
    selected_doctor = -1
    
def doc_add(doctors_list, doc_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry):
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                                  ', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=7,sticky='w')
    
    id = id_entry.get()
    name = name_entry.get()
    gend = gend_entry.get()
    dob = dob_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    dept = dept_entry.get()
    salary = salary_entry.get()

    # Validation
    valid_check = 0
    
    #Validate ID
    if len(id) == 0:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    elif utils.invalid_id(id, "D-") == 1:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for doctor in doctors_list:
            if doctor.get_id() == id:
                Label(entry_frame, bg='deep sky blue', fg='crimson', text='ID already exist', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
                valid_check += 1
                break
    
    # Validate Name
    if len(name) == 0:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1

    # Validate Gender
    if len(gend) == 0:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
    elif utils.invalid_gend(gend) == 1:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1

    # Validate Date of Birth
    if len(dob) == 0:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
    elif utils.invalid_dob(dob) == 1:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
    
    # Validate Phone:
    if len(phone) != 0:
        if utils.invalid_phone(phone) == 1:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=4,sticky='w')
            valid_check += 1

    if len(salary) != 0:
        if utils.invalid_salary(salary) == 1:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=7,sticky='w')
            valid_check += 1

    # If All Valid
    if valid_check == 0:
        # Add to doctors_list
        new_doc = Doctor(id, name, gend, dob)
        if len(phone) > 0:
            new_doc.set_phone(phone)
        if len(email) > 0:
            new_doc.set_email(email)
        if len(dept) > 0:
            new_doc.set_dept(dept)
        if len(salary) > 0:
            new_doc.set_salary(salary)
        doctors_list.append(new_doc)

        # Display on Treeview
        global doc_count
        doc_tree.insert(parent='', index = 'end', iid=doc_count, text='', values=(id, name, gend, dob))
        doc_count += 1

        # Empty Entry boxes
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        gend_entry.delete(0, END)
        dob_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        dept_entry.delete(0, END)
        salary_entry.delete(0, END)

def doc_remove(doctors_list, doc_tree):
    if len(doc_tree.selection())>0:
        selected_doc = doc_tree.selection()[0]
        doc_id = doc_tree.item(selected_doc, 'values')[0]
        for doctor in doctors_list:
            if doctor.get_id()== doc_id:
                doctors_list.remove(doctor)
                break
        doc_tree.delete(selected_doc)

def all_doc_remove(doc_tree, doctors_list):
    for doc in doc_tree.get_children():
        doc_tree.delete(doc)
    doctors_list.clear()

def doc_select(doctors_list, doc_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry):
    # Delete all Warnings
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                                  ', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=7,sticky='w')
    
    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    gend_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    dept_entry.delete(0, END)
    salary_entry.delete(0, END)

    # Show Selected Doctor Info
    if len(doc_tree.selection())>0:
        global selected_doctor
        selected_doctor = doc_tree.selection()[0]
        doc_id = doc_tree.item(selected_doctor, 'values')[0]
        for doctor in doctors_list:
            if doctor.get_id()== doc_id:
                id_entry.insert(0, doctor.get_id())
                name_entry.insert(0, doctor.get_name())
                gend_entry.insert(0, doctor.get_gend())
                dob_entry.insert(0, doctor.get_dob())
                phone_entry.insert(0, doctor.get_phone())
                email_entry.insert(0, doctor.get_email())
                dept_entry.insert(0, doctor.get_dept())
                salary_entry.insert(0, doctor.get_salary())
                break

def doc_update(doctors_list, doc_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry):
    global selected_doctor
    if selected_doctor != -1:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='                                  ', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=1,sticky='w')
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=4,sticky='w')
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=5,sticky='w')
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=6,sticky='w')
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=7,sticky='w')
        
        id = id_entry.get()
        name = name_entry.get()
        gend = gend_entry.get()
        dob = dob_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        dept = dept_entry.get()
        salary = salary_entry.get()
            
        # Validation
        valid_check = 0
        
        #Validate ID
        if len(id) == 0:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        elif utils.invalid_id(id, "D-") == 1:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            # check if new id is different from old id, if yes, check for duplication
            if id != doc_tree.item(selected_doctor, 'values')[0]:
                for doctor in doctors_list:
                    if doctor.get_id() == id:
                        Label(entry_frame, bg='deep sky blue', fg='crimson', text='ID already exist', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
                        valid_check += 1
                        break
        
        # Validate Name
        if len(name) == 0:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1

        # Validate Gender
        if len(gend) == 0:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        elif utils.invalid_gend(gend) == 1:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1

        # Validate Date of Birth
        if len(dob) == 0:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1
        elif utils.invalid_dob(dob) == 1:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1
        
        # Validate Phone:
        if len(phone) != 0:
            if utils.invalid_phone(phone) == 1:
                Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=4,sticky='w')
                valid_check += 1

        if len(salary) != 0:
            if utils.invalid_salary(salary) == 1:
                Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=7,sticky='w')
                valid_check += 1

        # If All Valid
        if valid_check == 0:
            for doctor in doctors_list:
                if doctor.get_id() == doc_tree.item(selected_doctor, 'values')[0]:
                    doctor.set_id(id)
                    doctor.set_name(name)
                    doctor.set_gend(gend)
                    doctor.set_dob(dob)
                    if len(phone) > 0:
                        doctor.set_phone(phone)
                    if len(email) > 0:
                        doctor.set_email(email)
                    if len(dept) > 0:
                        doctor.set_dept(dept)
                    if len(salary) > 0:
                        doctor.set_salary(salary)
                    break
            doc_tree.item(selected_doctor, text="", values = (id, name, gend, dob))
            selected_doctor = -1
        
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            gend_entry.delete(0, END)
            dob_entry.delete(0, END)
            phone_entry.delete(0, END)
            email_entry.delete(0, END)
            dept_entry.delete(0, END)
            salary_entry.delete(0, END)

def doc_press(window, fulwidth, fulheight, doctors_list):
    global selected_doctor
    selected_doctor = -1
    
    subwin = Toplevel(window)
    subwin.geometry("%dx%d" % (fulwidth, fulheight))
    icon = PhotoImage(file = "images/HIMS Icon.png")
    subwin.iconphoto(False, icon)
    subwin.title("Doctors Information Management")
    Frame(subwin, bg='deep sky blue').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)
    
    #=====================================================================================
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview",
        background = "silver",
        foreground = "black",
        rowheight = 25,
        font=("Ariel", 12),
        fieldbackground = "silver"
        )
    style.configure("Treeview.Heading", font=("Ariel", 16,'bold'))
    
    style.map('Treeview', background=[('selected', 'dark blue')])

    # Create TreeView List
    doc_tree = ttk.Treeview(subwin, selectmode='browse', show='headings')

    # Define columns
    doc_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth")

    # Format columns
    doc_tree.column("#0", width=0, stretch=NO)
    doc_tree.column("ID", anchor='center', width=75)
    doc_tree.column("Name",anchor='w', width=150)
    doc_tree.column("Gender",anchor='center', width=75)
    doc_tree.column("Date of Birth",anchor='center', width=125)

    # Create Headings
    doc_tree.heading("#0", text="")
    doc_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_doctor_by_column(doc_tree, doctors_list, "ID", False))
    doc_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_doctor_by_column(doc_tree, doctors_list, "Name", False))
    doc_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_doctor_by_column(doc_tree, doctors_list, "Gender", False))
    doc_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_doctor_by_column(doc_tree, doctors_list, "Date of Birth", False))

    doc_tree.bind('<Motion>', 'break')
    # Insert Data
    global doc_count
    doc_count = 0
    for doctor in doctors_list:
        doc_tree.insert(parent='', index = 'end', iid=doc_count, text='', values=(doctor.get_id(), doctor.get_name(), doctor.get_gend(), doctor.get_dob()))
        doc_count += 1
        
    doc_tree.place(x=fulwidth/2+50, y=50, height=fulheight-250, width=fulwidth/2-100)


    #=========================================================================================
    
    # Doctor Control
    Label(subwin, bg='deep sky blue', fg='white', text='DOCTORS MANAGEMENT', font=("Ariel", 20, 'bold')).place(x=50, y=25, width=fulwidth/2-100, height=50)
    Frame(subwin, bg='crimson').place(x=50, y=85, width=fulwidth/2-100, height=2)
    entry_frame = Frame(subwin, bg='deep sky blue')
    entry_frame.place(x=50, y=100, width=fulwidth/2-100, height=fulheight/2)
    Frame(subwin, bg='crimson').place(x=50, y=350, width=fulwidth/2-100, height=2)
    Label(subwin, text=' Entries marked with " * " must not be empty ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=360, height=30)
    Label(subwin, text=' ID must be " D-xxx " ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=380, height=30)
    Label(subwin, text=' Gender must be " M " or " F " ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=400, height=30)
    Label(subwin, text=' Date of Birth must be " dd/mm/yyyy " ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=420, height=30)
    Label(subwin, text=' Phone & Salary mustbe numbers ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=440, height=30)


    # Column 0: ( * )
    Label(entry_frame, bg='deep sky blue', fg='red', text='( * )', font=("Ariel", 14, 'bold')).grid(column=0, row=0)
    Label(entry_frame, bg='deep sky blue', fg='red', text='( * )', font=("Ariel", 14, 'bold')).grid(column=0, row=1)
    Label(entry_frame, bg='deep sky blue', fg='red', text='( * )', font=("Ariel", 14, 'bold')).grid(column=0, row=2)
    Label(entry_frame, bg='deep sky blue', fg='red', text='( * )', font=("Ariel", 14, 'bold')).grid(column=0, row=3)
    
    # Column 1: |
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=1, row=0)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=1, row=1)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=1, row=2)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=1, row=3)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=1, row=4)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=1, row=5)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=1, row=6)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=1, row=7)

    # Column 2: Atribute
    Label(entry_frame, bg='deep sky blue', fg='white', text=' - ID - ', font=("Ariel", 14, 'bold')).grid(column=2, row=0)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' - Name - ', font=("Ariel", 14, 'bold')).grid(column=2, row=1)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' - Gender - ', font=("Ariel", 14, 'bold')).grid(column=2, row=2)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' - DoB - ', font=("Ariel", 14, 'bold')).grid(column=2, row=3)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' - Phone - ', font=("Ariel", 14, 'bold')).grid(column=2, row=4)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' - Email - ', font=("Ariel", 14, 'bold')).grid(column=2, row=5)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' - Dept - ', font=("Ariel", 14, 'bold')).grid(column=2, row=6)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' - Salary - ', font=("Ariel", 14, 'bold')).grid(column=2, row=7)

    # Column 3: |
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=3, row=0)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=3, row=1)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=3, row=2)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=3, row=3)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=3, row=4)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=3, row=5)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=3, row=6)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=3, row=7)
    
    # Column 4: Entries
    id_entry = Entry(entry_frame)
    id_entry.grid(column=4,row=0)

    name_entry = Entry(entry_frame)
    name_entry.grid(column=4,row=1)

    gend_entry = Entry(entry_frame)
    gend_entry.grid(column=4,row=2)

    dob_entry = Entry(entry_frame)
    dob_entry.grid(column=4,row=3)

    phone_entry = Entry(entry_frame)
    phone_entry.grid(column=4,row=4)

    email_entry = Entry(entry_frame)
    email_entry.grid(column=4,row=5)

    dept_entry = Entry(entry_frame)
    dept_entry.grid(column=4,row=6)

    salary_entry = Entry(entry_frame)
    salary_entry.grid(column=4,row=7)

    # Column 5: |
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=5, row=0)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=5, row=1)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=5, row=2)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=5, row=3)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=5, row=4)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=5, row=5)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=5, row=6)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=5, row=7)

    # Buttons
    add_doctor = Button(subwin, text='ADD DOCTOR',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: doc_add(doctors_list, doc_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry,phone_entry,email_entry,dept_entry,salary_entry))
    add_doctor.place(x=50, y=fulheight-75-85-10-50, width=150, height=50)

    update_doctor = Button(subwin, text='UPDATE',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: doc_update(doctors_list, doc_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry,phone_entry,email_entry,dept_entry,salary_entry))
    update_doctor.place(x=fulwidth/2-50-150, y=fulheight-75-85-10-50, width=150, height=50)

    clear = Button(subwin, text='CLEAR',anchor='center',font=("Ariel", 12,'bold'), fg='red', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(entry_frame, id_entry, name_entry, gend_entry, dob_entry,phone_entry,email_entry,dept_entry,salary_entry))
    clear.place(x=50,y=fulheight-75-85, width=fulwidth/2-100, height=50)

    remove_doctor = Button(subwin, text='REMOVE SELECTED',anchor='center',font=("Ariel", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: doc_remove(doctors_list, doc_tree))
    remove_doctor.place(x=fulwidth/4*3-100, y=fulheight-75-85, width=200, height=50)

    remove_all_doctor = Button(subwin, text='REMOVE ALL',anchor='center',font=("Ariel", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: all_doc_remove(doc_tree, doctors_list))
    remove_all_doctor.place(x=fulwidth-50-150, y=fulheight-75-85, width=150, height=50)

    select_doctor = Button(subwin, text='SELECT',anchor='center',font=("Ariel", 12,'bold'), bg='deep sky blue',fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: doc_select(doctors_list, doc_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry,phone_entry,email_entry,dept_entry,salary_entry))
    select_doctor.place(x=fulwidth/2+50, y=fulheight-75-85, width=150, height=50)

    show_patients = Button(subwin, text='SHOW PATIENTS',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white')
    show_patients.place(x=fulwidth/4*1-100, y=fulheight-75-85-10-50, width=200, height=50)

