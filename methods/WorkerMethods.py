from domains.People import *
from domains.Relations import *
from tkinter import *
from tkinter import ttk
from tk import *
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

    # Set selected_worker to -1
    global selected_worker
    selected_worker = -1
    
def wor_add(workers_list, wor_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry):
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
    elif utils.invalid_id(id, "W-") == 1:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for worker in workers_list:
            if worker.get_id() == id:
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
        # Add to workers_list
        new_wor = Worker(id, name, gend, dob)
        if len(phone) > 0:
            new_wor.set_phone(phone)
        if len(email) > 0:
            new_wor.set_email(email)
        if len(dept) > 0:
            new_wor.set_dept(dept)
        if len(salary) > 0:
            new_wor.set_salary(salary)
        workers_list.append(new_wor)

        # Display on Treeview
        wor_tree.insert(parent='', index = 'end', iid=id, text='', values=(id, name, gend, dob))

        # Empty Entry boxes
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        gend_entry.delete(0, END)
        dob_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        dept_entry.delete(0, END)
        salary_entry.delete(0, END)

def wor_remove(workers_list, wor_tree):
    if len(wor_tree.selection())>0:
        selected_wor = wor_tree.selection()[0]
        worker_id = wor_tree.item(selected_wor, 'values')[0]
        for worker in workers_list:
            if worker.get_id()== worker_id:
                workers_list.remove(worker)
                break
        wor_tree.delete(selected_wor)

def all_wor_remove(wor_tree, workers_list):
    for wor in wor_tree.get_children():
        wor_tree.delete(wor)
    workers_list.clear()

def wor_select(workers_list, wor_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry):
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

    # Show Selected Worker Info
    if len(wor_tree.selection())>0:
        global selected_worker
        selected_worker = wor_tree.selection()[0]
        wor_id = wor_tree.item(selected_worker, 'values')[0]
        for worker in workers_list:
            if worker.get_id()== wor_id:
                id_entry.insert(0, worker.get_id())
                name_entry.insert(0, worker.get_name())
                gend_entry.insert(0, worker.get_gend())
                dob_entry.insert(0, worker.get_dob())
                phone_entry.insert(0, worker.get_phone())
                email_entry.insert(0, worker.get_email())
                dept_entry.insert(0, worker.get_dept())
                salary_entry.insert(0, worker.get_salary())
                break

def wor_update(workers_list, wor_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry):
    global selected_worker
    if selected_worker != -1:
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
        elif utils.invalid_id(id, "W-") == 1:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            # check if new id is different from old id, if yes, check for duplication
            if id != wor_tree.item(selected_worker, 'values')[0]:
                for worker in workers_list:
                    if worker.get_id() == id:
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
        if len(phone) != 0 and phone != '_':
            if utils.invalid_phone(phone) == 1:
                Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=4,sticky='w')
                valid_check += 1

        if len(salary) != 0:
            if utils.invalid_salary(salary) == 1:
                Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=7,sticky='w')
                valid_check += 1

        # If All Valid
        if valid_check == 0:
            for worker in workers_list:
                if worker.get_id() == wor_tree.item(selected_worker, 'values')[0]:
                    worker.set_id(id)
                    worker.set_name(name)
                    worker.set_gend(gend)
                    worker.set_dob(dob)
                    if len(phone) > 0:
                        worker.set_phone(phone)
                    elif len(phone) == 0:
                        worker.set_phone('_')
                    if len(email) > 0:
                        worker.set_email(email)
                    elif len(email) == 0:
                        worker.set_email('_')
                    if len(dept) > 0:
                        worker.set_dept(dept)
                    elif len(dept) == 0:
                        worker.set_dept('_')
                    if len(salary) > 0:
                        worker.set_salary(salary)
                    elif len(salary) == 0:
                        worker.set_salary(0)
                    break
            wor_tree.item(selected_worker, text="", values = (id, name, gend, dob))
            selected_worker = -1
        
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            gend_entry.delete(0, END)
            dob_entry.delete(0, END)
            phone_entry.delete(0, END)
            email_entry.delete(0, END)
            dept_entry.delete(0, END)
            salary_entry.delete(0, END)

def wor_press(window, fulwidth, fulheight, workers_list):
    global selected_worker
    selected_worker = -1

    wor_subwin = Toplevel(window)
    wor_subwin.geometry("%dx%d" % (fulwidth, fulheight))
    icon = PhotoImage(file = "images/HIMS Icon.png")
    wor_subwin.iconphoto(False, icon)
    wor_subwin.title("Workers Information Management")
    Frame(wor_subwin, bg='deep sky blue').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)
    

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
    wor_tree = ttk.Treeview(wor_subwin, selectmode='browse', show='headings')

    # Define columns
    wor_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth")

    # Format columns
    wor_tree.column("#0", width=0, stretch=NO)
    wor_tree.column("ID", anchor='center', width=75)
    wor_tree.column("Name",anchor='w', width=150)
    wor_tree.column("Gender",anchor='center', width=75)
    wor_tree.column("Date of Birth",anchor='center', width=125)

    # Create Headings
    wor_tree.heading("#0", text="")
    wor_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_people_list_by_column(wor_tree, workers_list, "ID", False))
    wor_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_people_list_by_column(wor_tree, workers_list, "Name", False))
    wor_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_people_list_by_column(wor_tree, workers_list, "Gender", False))
    wor_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_people_list_by_column(wor_tree, workers_list, "Date of Birth", False))

    wor_tree.bind('<Motion>', 'break')
    
    # Insert Data
    for worker in workers_list:
        wor_tree.insert(parent='', index = 'end', iid=worker.get_id(), text='', values=(worker.get_id(), worker.get_name(), worker.get_gend(), worker.get_dob()))
        
    wor_tree.place(x=fulwidth/2+50, y=50, height=fulheight-250, width=fulwidth/2-100)
    #=========================================================================================
    
    # Worker Control
    Label(wor_subwin, bg='deep sky blue', fg='white', text='WORKERS MANAGEMENT', font=("Ariel", 20, 'bold')).place(x=50, y=25, width=fulwidth/2-100, height=50)
    Frame(wor_subwin, bg='crimson').place(x=50, y=85, width=fulwidth/2-100, height=2)
    entry_frame = Frame(wor_subwin, bg='deep sky blue')
    entry_frame.place(x=50, y=100, width=fulwidth/2-100, height=fulheight/2)
    Frame(wor_subwin, bg='crimson').place(x=50, y=350, width=fulwidth/2-100, height=2)
    Label(wor_subwin, text=' Entries marked with " * " must not be empty ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=360, height=30)
    Label(wor_subwin, text=' ID must be " W-xxx " ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=385, height=30)
    Label(wor_subwin, text=' Gender must be " M " or " F " ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=410, height=30)
    Label(wor_subwin, text=' Date of Birth must be " dd/mm/yyyy " ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=435, height=30)
    Label(wor_subwin, text=' Phone & Salary must be numbers ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=460, height=30)


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
    add_worker_button = Button(wor_subwin, text='ADD WORKER',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: wor_add(workers_list, wor_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry))
    add_worker_button.place(x=50, y=fulheight-75-85-10-50, width=250, height=50)

    update_worker_button = Button(wor_subwin, text='UPDATE',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: wor_update(workers_list, wor_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry))
    update_worker_button.place(x=300, y=fulheight-75-85-10-50, width=250, height=50)

    clear_button = Button(wor_subwin, text='CLEAR',anchor='center',font=("Ariel", 12,'bold'), fg='red', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry))
    clear_button.place(x=50, y=fulheight-75-85-10, width=500, height=50)

    remove_worker_button = Button(wor_subwin, text='REMOVE SELECTED',anchor='center',font=("Ariel", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: wor_remove(workers_list, wor_tree))
    remove_worker_button.place(x=fulwidth/4*3-100, y=fulheight-75-85, width=200, height=50)

    remove_all_worker_button = Button(wor_subwin, text='REMOVE ALL',anchor='center',font=("Ariel", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: all_wor_remove(wor_tree, workers_list))
    remove_all_worker_button.place(x=fulwidth-50-150, y=fulheight-75-85, width=150, height=50)

    select_worker_button = Button(wor_subwin, text='SELECT',anchor='center',font=("Ariel", 12,'bold'), bg='deep sky blue',fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: wor_select(workers_list, wor_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry))
    select_worker_button.place(x=fulwidth/2+50, y=fulheight-75-85, width=150, height=50)