from domains.People import *
from domains.Relations import *
from domains.Medicine import *
from tkinter import *
from tkinter import ttk
from tk import *
import utils

def clear_entry(entry_frame, id_entry, name_entry, price_entry, stock_entry, description_entry):
    # Delete all Warnings
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                                  ', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')

    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    price_entry.delete(0, END)
    stock_entry.delete(0, END)
    description_entry.delete('1.0', END)

    # Set selected_patient to -1
    global selected_medicine
    selected_medicine = -1

def med_add(medicines_list, med_tree, entry_frame, id_entry, name_entry, price_entry, stock_entry, description_entry):
    # Delete all Warnings
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                                  ', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')

    # Read Inputs
    id = id_entry.get()
    name = name_entry.get()
    price = price_entry.get()
    stock = stock_entry.get()
    description = description_entry.get("1.0",'end-1c')

    # Validation
    valid_check = 0

    # Validate ID
    if len(id) == 0:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    elif utils.invalid_id(id, "M-") == 1:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for medicine in medicines_list:
            if medicine.get_id() == id:
                Label(entry_frame, bg='deep sky blue', fg='crimson', text='ID already exist', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
                valid_check += 1
                break

    # Validate Name
    if len(name) == 0:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1

    # Validate Price
    if len(price) == 0:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
    elif utils.invalid_price(price) == 1:
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1

    # Validate Stock
    if len(stock) != 0:
        if utils.invalid_stock(stock) == 1:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1

    # If ALL valid:
    if valid_check == 0:
        # Add to medicines_list:
        new_med = Medicine(id,name,price)
        if len(stock) >0:
            new_med.set_stock(stock)
        if len(description)>0:
            new_med.set_description(description)
        medicines_list.append(new_med)

        # Display on Treeview
        med_tree.insert(parent='', index = 'end', iid=id, text='', values=(id, name, price, stock))


        # Empty Entry boxes
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        price_entry.delete(0, END)
        stock_entry.delete(0, END)
        description_entry.delete('1.0', END)

def med_remove(medicines_list, med_tree, pa_med_list):
    if len(med_tree.selection())>0:
        selected_med = med_tree.selection()[0]
        medicine_id = med_tree.item(selected_med, 'values')[0]

        for relation in pa_med_list:
            if relation.get_MedicineID() == medicine_id:
                pa_med_list.remove(relation)

        for medicine in medicines_list:
            if medicine.get_id()== medicine_id:
                medicines_list.remove(medicine)
                break

        med_tree.delete(selected_med)

def all_med_remove(med_tree, medicines_list, pa_med_list):
    for medicine in med_tree.get_children():
        med_tree.delete(medicine)
    pa_med_list.clear()
    medicines_list.clear()

def med_select(medicines_list, med_tree, entry_frame, id_entry, name_entry, price_entry, stock_entry, description_entry):
    # Delete all Warnings
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                                  ', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')

    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    price_entry.delete(0, END)
    stock_entry.delete(0, END)
    description_entry.delete('1.0', END)

    # Show Selected Patient Info
    if len(med_tree.selection())>0:
        global selected_medicine
        selected_medicine = med_tree.selection()[0]
        medicine_id = med_tree.item(selected_medicine, 'values')[0]

        for medicine in medicines_list:
            if medicine.get_id()== medicine_id:
                id_entry.insert(0, medicine.get_id())
                name_entry.insert(0, medicine.get_name())
                price_entry.insert(0, medicine.get_price())
                stock_entry.insert(0, medicine.get_stock())
                description_entry.insert('0.1', medicine.get_description())
                break

def med_update(medicines_list, pa_med_list, med_tree, entry_frame, id_entry, name_entry, price_entry, stock_entry, description_entry):
    global selected_medicine
    if selected_medicine != -1:
        # Delete all Warnings
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='                                  ', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=1,sticky='w')
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
        Label(entry_frame, bg='deep sky blue', fg='crimson', text='                   ', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')

        # Read Inputs
        id = id_entry.get()
        name = name_entry.get()
        price = price_entry.get()
        stock = stock_entry.get()
        description = description_entry.get("1.0",'end-1c')

        # Validation
        valid_check = 0

        # Validate ID
        if len(id) == 0:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        elif utils.invalid_id(id, "M-") == 1:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            if id != med_tree.item(selected_medicine, 'values')[0]:
                for medicine in medicines_list:
                    if medicine.get_id() == id:
                        Label(entry_frame, bg='deep sky blue', fg='crimson', text='ID already exist', font=("Ariel", 14, 'bold')).grid(column=6,row=0,sticky='w')
                        valid_check += 1
                        break

        # Validate Name
        if len(name) == 0:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1

        # Validate Price
        if len(price) == 0:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        elif utils.invalid_price(price) == 1:
            Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1

        # Validate Stock
        if len(stock) != 0:
            if utils.invalid_stock(stock) == 1:
                Label(entry_frame, bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=6,row=3,sticky='w')
                valid_check += 1

        # If ALL Valid
        if valid_check == 0:
            for medicine in medicines_list:
                if medicine.get_id() == med_tree.item(selected_medicine, 'values')[0]:
                    medicine.set_id(id)
                    medicine.set_name(name)
                    medicine.set_price(price)
                    if len(stock) > 0:
                        medicine.set_stock(stock)
                    elif len(stock) == 0:
                        medicine.set_stock(0)
                    medicine.set_description(description)
            for relation in pa_med_list:
                if relation.get_MedicineID() == med_tree.item(selected_medicine, 'values')[0]:
                    relation.set_MedicineID(id)

            med_tree.item(selected_medicine, text="", values = (id, name, price, stock))
            selected_medicine = -1

            # Empty Entry boxes
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            price_entry.delete(0, END)
            stock_entry.delete(0, END)
            description_entry.delete('1.0', END)

def patients_assignment(med_subwin, med_tree, fulwidth, fulheight, pa_med_list, patients_list, assigned_patients_list, unassigned_patients_list):
    if selected_medicine != -1:    
        medpa_subwin = Toplevel(med_subwin)
        medpa_subwin.geometry("%dx%d" % (fulwidth, fulheight))
        icon = PhotoImage(file = "images/HIMS Icon.png")
        medpa_subwin.iconphoto(False, icon)
        medpa_subwin.title("Medicine _ Patients Assignment")
        Frame(medpa_subwin, bg='deep sky blue').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)
        Label(medpa_subwin, text='ASSIGNED PATIENTS', bg='deep sky blue', fg='white', font=("Ariel", 20, 'bold')).place(x=50,y=50,width=fulwidth/2-100,height=50)
        Label(medpa_subwin, text='UNASSIGNED PATIENTS', fg='deep sky blue', font=("Ariel", 20, 'bold')).place(x=fulwidth/2+50,y=50,width=fulwidth/2-100,height=50)

        # Create list of assigned and unassigned patients for selected doctor
        assigned_patients_list.clear()
        unassigned_patients_list.clear()

        medicine_id = med_tree.item(selected_medicine, 'values')[0]
        temp_list = []
        for relation in pa_med_list:
            if relation.get_MedicineID() == medicine_id:
                temp_list.append(relation)
        for patient in patients_list:
            check = 0
            for relation in temp_list:
                if patient.get_id() == relation.get_PatientID():
                    check += 1
                    break
            if check == 0:
                unassigned_patients_list.append(patient)
            else:
                assigned_patients_list.append(patient)
        temp_list.clear()

        # Unassigned treeview
        # create Treeview
        unassigned_patients_tree = ttk.Treeview(medpa_subwin, selectmode='browse', show='headings')

        # define columns
        unassigned_patients_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth")

        # Format columns
        unassigned_patients_tree.column("#0", width=0, stretch=NO)
        unassigned_patients_tree.column("ID", anchor='center', width=75)
        unassigned_patients_tree.column("Name",anchor='w', width=150)
        unassigned_patients_tree.column("Gender",anchor='center', width=75)
        unassigned_patients_tree.column("Date of Birth",anchor='center', width=125)

        # Create Headings
        unassigned_patients_tree.heading("#0", text="")
        unassigned_patients_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_people_list_by_column(unassigned_patients_tree, unassigned_patients_list, "ID", False))
        unassigned_patients_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_people_list_by_column(unassigned_patients_tree, unassigned_patients_list, "Name", False))
        unassigned_patients_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_people_list_by_column(unassigned_patients_tree, unassigned_patients_list, "Gender", False))
        unassigned_patients_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_people_list_by_column(unassigned_patients_tree, unassigned_patients_list, "Date of Birth", False))

        unassigned_patients_tree.bind('<Motion>', 'break')

        # Insert Data
        global unassigned_patients_count
        unassigned_patients_count = 0
        for patient in unassigned_patients_list:
            unassigned_patients_tree.insert(parent='', index = 'end', iid=patient.get_id(), text='', values=(patient.get_id(), patient.get_name(), patient.get_gend(), patient.get_dob()))
            unassigned_patients_count += 1

        unassigned_patients_tree.place(x=fulwidth/2+50, y=100, height=fulheight-300, width=fulwidth/2-100)

        #==========================================================================================
        # Assigned treeview
        assigned_patients_tree = ttk.Treeview(medpa_subwin, selectmode='browse', show='headings')

        # define columns
        assigned_patients_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth")

        # Format columns
        assigned_patients_tree.column("#0", width=0, stretch=NO)
        assigned_patients_tree.column("ID", anchor='center', width=75)
        assigned_patients_tree.column("Name",anchor='w', width=150)
        assigned_patients_tree.column("Gender",anchor='center', width=75)
        assigned_patients_tree.column("Date of Birth",anchor='center', width=125)

        # Create Headings
        assigned_patients_tree.heading("#0", text="")
        assigned_patients_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_people_list_by_column(assigned_patients_tree, assigned_patients_list, "ID", False))
        assigned_patients_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_people_list_by_column(assigned_patients_tree, assigned_patients_list, "Name", False))
        assigned_patients_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_people_list_by_column(assigned_patients_tree, assigned_patients_list, "Gender", False))
        assigned_patients_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_people_list_by_column(assigned_patients_tree, assigned_patients_list, "Date of Birth", False))

        assigned_patients_tree.bind('<Motion>', 'break')

        # Insert Data
        global assigned_patients_count
        assigned_patients_count = 0
        for patient in assigned_patients_list:
            assigned_patients_tree.insert(parent='', index = 'end', iid=patient.get_id(), text='', values=(patient.get_id(), patient.get_name(), patient.get_gend(), patient.get_dob()))
            assigned_patients_count += 1

        assigned_patients_tree.place(x=50, y=100, height=fulheight-300, width=fulwidth/2-100)

        # ===============================================================================

        Label(medpa_subwin, text=f"COUNT: {assigned_patients_count}", anchor='e', bg='deep sky blue', fg='black', font=("Ariel", 16, 'bold')).place(x=fulwidth/4+50,y=fulheight-150,width=200,height=50)
        Label(medpa_subwin, text=f"COUNT: {unassigned_patients_count}", anchor='e',fg='black', font=("Ariel", 16, 'bold')).place(x=fulwidth/4*3+50,y=fulheight-150,width=200,height=50)

        # Buttons
        assign_patient_button = Button(medpa_subwin, text='ASSIGN PATIENT', font=("Ariel", 16, 'bold'), fg='white', bg='deep sky blue', relief='ridge',
            activebackground='dark blue', activeforeground='white', command=lambda: assign_patient(medpa_subwin, fulwidth, fulheight, assigned_patients_tree, unassigned_patients_tree, assigned_patients_list, unassigned_patients_list, patients_list, medicine_id, pa_med_list))
        assign_patient_button.place(x=fulwidth/2+50, y=fulheight-150, width=250, height=50)

        unassign_patient_button = Button(medpa_subwin, text='UNASSIGN PATIENT', font=("Ariel", 16, 'bold'), fg='deep sky blue', relief='ridge',
            activebackground='dark blue', activeforeground='white', command=lambda: unassign_patient(medpa_subwin, fulwidth, fulheight, assigned_patients_tree, unassigned_patients_tree, assigned_patients_list, unassigned_patients_list, patients_list, medicine_id, pa_med_list))
        unassign_patient_button.place(x=50, y=fulheight-150, width=250, height=50)

def assign_patient(medpa_subwin, fulwidth, fulheight, assigned_patients_tree, unassigned_patients_tree, assigned_patients_list, unassigned_patients_list, patients_list, medicine_id, pa_med_list):
    if len(unassigned_patients_tree.selection())>0:
        selected_unassigned_patient = unassigned_patients_tree.selection()[0]
        patient_id = unassigned_patients_tree.item(selected_unassigned_patient, 'values')[0]

        pa_med_list.append(Pa_Med(patient_id, medicine_id))
        global unassigned_patients_count
        global assigned_patients_count

        assigned_patients_tree.insert(parent='', index = 'end', iid=patient_id, text='', values=(unassigned_patients_tree.item(selected_unassigned_patient, 'values')))
        unassigned_patients_tree.delete(selected_unassigned_patient)
        
        for patient in patients_list:
            if patient.get_id()==patient_id:
                assigned_patients_list.append(patient)
                break

        for patient in unassigned_patients_list:
            if patient.get_id()==patient_id:
                unassigned_patients_list.remove(patient)
                break
        unassigned_patients_count -= 1
        assigned_patients_count += 1
        Label(medpa_subwin, text=f"COUNT: {assigned_patients_count}", anchor='e', bg='deep sky blue', fg='black', font=("Ariel", 16, 'bold')).place(x=fulwidth/4+50,y=fulheight-150,width=200,height=50)
        Label(medpa_subwin, text=f"COUNT: {unassigned_patients_count}", anchor='e',fg='black', font=("Ariel", 16, 'bold')).place(x=fulwidth/4*3+50,y=fulheight-150,width=200,height=50)

def unassign_patient(medpa_subwin, fulwidth, fulheight, assigned_patients_tree, unassigned_patients_tree, assigned_patients_list, unassigned_patients_list, patients_list, medicine_id, pa_med_list):
    if len(assigned_patients_tree.selection())>0:
        selected_assigned_patient = assigned_patients_tree.selection()[0]
        patient_id = assigned_patients_tree.item(selected_assigned_patient, 'values')[0]

        for relation in pa_med_list:
            if relation.get_PatientID() == patient_id and relation.get_MedicineID() == medicine_id:
                pa_med_list.remove(relation)
    
        global unassigned_patients_count
        global assigned_patients_count

        unassigned_patients_tree.insert(parent='', index = 'end', iid=patient_id, text='', values=(assigned_patients_tree.item(selected_assigned_patient, 'values')))
        assigned_patients_tree.delete(selected_assigned_patient)

        for patient in patients_list:
            if patient.get_id()==patient_id:
                unassigned_patients_list.append(patient)
                break

        for patient in assigned_patients_list:
            if patient.get_id()==patient_id:
                assigned_patients_list.remove(patient)
                break
        unassigned_patients_count += 1
        assigned_patients_count -= 1
            
        Label(medpa_subwin, text=f"COUNT: {assigned_patients_count}", anchor='e', bg='deep sky blue', fg='black', font=("Ariel", 16, 'bold')).place(x=fulwidth/4+50,y=fulheight-150,width=200,height=50)
        Label(medpa_subwin, text=f"COUNT: {unassigned_patients_count}", anchor='e',fg='black', font=("Ariel", 16, 'bold')).place(x=fulwidth/4*3+50,y=fulheight-150,width=200,height=50)

def med_press(window, fulwidth, fulheight, medicines_list, patients_list, pa_med_list):
    global selected_medicine
    selected_medicine = -1

    med_subwin = Toplevel(window)
    med_subwin.geometry("%dx%d" % (fulwidth, fulheight))
    icon = PhotoImage(file = "images/HIMS Icon.png")
    med_subwin.iconphoto(False, icon)
    med_subwin.title("Medicines Information Management")
    Frame(med_subwin, bg='deep sky blue').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)
    
    assigned_patients_list = []
    unassigned_patients_list = []

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
    med_tree = ttk.Treeview(med_subwin, selectmode='browse', show='headings')

    # Define columns
    med_tree['columns'] = ("ID", "Name", "Price", "Stock")

    # Format columns
    med_tree.column("#0", width=0, stretch=NO)
    med_tree.column("ID", anchor='center', width=75)
    med_tree.column("Name",anchor='w', width=150)
    med_tree.column("Price",anchor='e', width=100)
    med_tree.column("Stock",anchor='e', width=100)

    # Create Headings
    med_tree.heading("#0", text="")
    med_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_medicines_list_by_column(med_tree, medicines_list, "ID", False))
    med_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_medicines_list_by_column(med_tree, medicines_list, "Name", False))
    med_tree.heading("Price", text="Price", anchor='center', command= lambda: utils.sort_medicines_list_by_column(med_tree, medicines_list, "Price", False))
    med_tree.heading("Stock", text="Stock", anchor='center', command= lambda: utils.sort_medicines_list_by_column(med_tree, medicines_list, "Stock", False))

    med_tree.bind('<Motion>', 'break')

    # Insert Data
    for medicine in medicines_list:
        med_tree.insert(parent='', index = 'end', iid=medicine.get_id(), text='', values=(medicine.get_id(), medicine.get_name(), medicine.get_price(), medicine.get_stock()))
        
    med_tree.place(x=fulwidth/2+50, y=50, height=fulheight-250, width=fulwidth/2-100)

    #=====================================================================================
    Label(med_subwin, bg='deep sky blue', fg='white', text='MEDICINES MANAGEMENT', font=("Ariel", 20, 'bold')).place(x=50, y=25, width=fulwidth/2-100, height=50)
    Frame(med_subwin, bg='crimson').place(x=50, y=85, width=fulwidth/2-100, height=2)
    entry_frame = Frame(med_subwin, bg='deep sky blue')
    entry_frame.place(x=50, y=100, width=fulwidth/2-100, height=fulheight/2)
    Frame(med_subwin, bg='crimson').place(x=50, y=350, width=fulwidth/2-100, height=2)
    text_frame = Frame(med_subwin, bg='deep sky blue')
    text_frame.place(x=50, y=fulheight/2-140, width=fulwidth/2-100, height=115)

    # Column 0: ( * )
    Label(entry_frame, bg='deep sky blue', fg='red', text='( * )', font=("Ariel", 14, 'bold')).grid(column=0, row=0)
    Label(entry_frame, bg='deep sky blue', fg='red', text='( * )', font=("Ariel", 14, 'bold')).grid(column=0, row=1)
    Label(entry_frame, bg='deep sky blue', fg='red', text='( * )', font=("Ariel", 14, 'bold')).grid(column=0, row=2)

    # Column 1: |
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=1, row=0)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=1, row=1)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=1, row=2)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=1, row=3)

    # Column 2: Atribute
    Label(entry_frame, bg='deep sky blue', fg='white', text=' - ID - ', font=("Ariel", 14, 'bold')).grid(column=2, row=0)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' - Name - ', font=("Ariel", 14, 'bold')).grid(column=2, row=1)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' - Price - ', font=("Ariel", 14, 'bold')).grid(column=2, row=2)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' - Stock - ', font=("Ariel", 14, 'bold')).grid(column=2, row=3)

    # Column 3: |
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=3, row=0)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=3, row=1)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=3, row=2)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=3, row=3)

    # Column 4: Entries
    id_entry = Entry(entry_frame)
    id_entry.grid(column=4,row=0)

    name_entry = Entry(entry_frame)
    name_entry.grid(column=4,row=1)

    price_entry = Entry(entry_frame)
    price_entry.grid(column=4,row=2)

    stock_entry = Entry(entry_frame)
    stock_entry.grid(column=4,row=3)

    # Column 5: |
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=5, row=0)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=5, row=1)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=5, row=2)
    Label(entry_frame, bg='deep sky blue', fg='white', text=' | ', font=("Ariel", 14, 'bold')).grid(column=5, row=3)

    # Description
    Label(text_frame, bg='deep sky blue', fg='white', text=' - Description - ', font=("Ariel", 14, 'bold')).grid(column=0, row=0)
    description_entry = Text(text_frame, width=65, height=5)
    description_entry.grid(row=1, column=0, columnspan=5)

    #==================================================================================

    Label(med_subwin, text='  - Entries marked with " * " must not be empty ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=360, height=30)
    Label(med_subwin, text='  - ID must be " M-xxx " ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=385, height=30)
    Label(med_subwin, text='  - Price & Stock must be a number ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=410, height=30)

    add_medicine_button = Button(med_subwin, text='ADD MEDICINE',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: med_add(medicines_list, med_tree, entry_frame, id_entry, name_entry, price_entry, stock_entry, description_entry))
    add_medicine_button.place(x=50, y=fulheight-75-85-10-50, width=150, height=50)

    update_medicine_button = Button(med_subwin, text='UPDATE',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: med_update(medicines_list, pa_med_list, med_tree, entry_frame, id_entry, name_entry, price_entry, stock_entry, description_entry))
    update_medicine_button.place(x=fulwidth/2-50-150, y=fulheight-75-85-10-50, width=150, height=50)

    clear_button = Button(med_subwin, text='CLEAR',anchor='center',font=("Ariel", 12,'bold'), fg='red', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(entry_frame, id_entry, name_entry, price_entry, stock_entry, description_entry))
    clear_button.place(x=fulwidth/4*1-100, y=fulheight-75-85-10-50, width=200, height=50)

    remove_medicine_button = Button(med_subwin, text='REMOVE SELECTED',anchor='center',font=("Ariel", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: med_remove(medicines_list, med_tree, pa_med_list))
    remove_medicine_button.place(x=fulwidth/4*3-100, y=fulheight-75-85, width=200, height=50)

    remove_all_medicine_button = Button(med_subwin, text='REMOVE ALL',anchor='center',font=("Ariel", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: all_med_remove(med_tree, medicines_list, pa_med_list))
    remove_all_medicine_button.place(x=fulwidth-50-150, y=fulheight-75-85, width=150, height=50)

    select_medicine_button = Button(med_subwin, text='SELECT',anchor='center',font=("Ariel", 12,'bold'), bg='deep sky blue',fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: med_select(medicines_list, med_tree, entry_frame, id_entry, name_entry, price_entry, stock_entry, description_entry))
    select_medicine_button.place(x=fulwidth/2+50, y=fulheight-75-85, width=150, height=50)

    patients_assignment_button = Button(med_subwin, text='PATIENTS ASSIGNMENT',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: patients_assignment(med_subwin, med_tree, fulwidth, fulheight, pa_med_list, patients_list, assigned_patients_list, unassigned_patients_list))
    patients_assignment_button.place(x=50,y=fulheight-75-85, width=fulwidth/2-100, height=50)