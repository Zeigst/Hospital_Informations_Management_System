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

    # Set selected_doctor to -1
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
        doc_tree.insert(parent='', index = 'end', iid=id, text='', values=(id, name, gend, dob))

        # Empty Entry boxes
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        gend_entry.delete(0, END)
        dob_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        dept_entry.delete(0, END)
        salary_entry.delete(0, END)

def doc_remove(doctors_list, doc_tree, pa_doc_list):
    if len(doc_tree.selection())>0:
        selected_doc = doc_tree.selection()[0]
        doctor_id = doc_tree.item(selected_doc, 'values')[0]
        for relation in pa_doc_list:
            if relation.get_DoctorID() == doctor_id:
                pa_doc_list.remove(relation)
        
        for doctor in doctors_list:
            if doctor.get_id()== doctor_id:
                doctors_list.remove(doctor)
                break
        doc_tree.delete(selected_doc)

def all_doc_remove(doc_tree, doctors_list, pa_doc_list):
    for doc in doc_tree.get_children():
        doc_tree.delete(doc)
    pa_doc_list.clear()
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

def doc_update(doctors_list, pa_doc_list, doc_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry):
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
            for doctor in doctors_list:
                if doctor.get_id() == doc_tree.item(selected_doctor, 'values')[0]:
                    doctor.set_id(id)
                    doctor.set_name(name)
                    doctor.set_gend(gend)
                    doctor.set_dob(dob)
                    if len(phone) > 0:
                        doctor.set_phone(phone)
                    elif len(phone) == 0:
                        doctor.set_phone('_')
                    if len(email) > 0:
                        doctor.set_email(email)
                    elif len(email) == 0:
                        doctor.set_email('_')
                    if len(dept) > 0:
                        doctor.set_dept(dept)
                    elif len(dept) == 0:
                        doctor.set_dept('_')
                    if len(salary) > 0:
                        doctor.set_salary(salary)
                    elif len(salary) == 0:
                        doctor.set_salary(0)
                    break
            
            for relation in pa_doc_list:
                if relation.get_DoctorID() == doc_tree.item(selected_doctor, 'values')[0]:
                    relation.set_DoctorID(id)
                    
            
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

def patients_assignment(doc_subwin, doc_tree, fulwidth, fulheight, pa_doc_list, patients_list, assigned_patients_list, unassigned_patients_list):
    if selected_doctor != -1:    
        docpa_subwin = Toplevel(doc_subwin)
        docpa_subwin.geometry("%dx%d" % (fulwidth, fulheight))
        icon = PhotoImage(file = "images/HIMS Icon.png")
        docpa_subwin.iconphoto(False, icon)
        docpa_subwin.title("Patients Assignment")
        Frame(docpa_subwin, bg='deep sky blue').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)
        Label(docpa_subwin, text='ASSIGNED PATIENTS', bg='deep sky blue', fg='white', font=("Ariel", 20, 'bold')).place(x=50,y=50,width=fulwidth/2-100,height=50)
        Label(docpa_subwin, text='UNASSIGNED PATIENTS', fg='deep sky blue', font=("Ariel", 20, 'bold')).place(x=fulwidth/2+50,y=50,width=fulwidth/2-100,height=50)

        # Create list of assigned and unassigned patients for selected doctor
        assigned_patients_list.clear()
        unassigned_patients_list.clear()

        doctor_id = doc_tree.item(selected_doctor, 'values')[0]
        temp_list = []
        for relation in pa_doc_list:
            if relation.get_DoctorID() == doctor_id:
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
        unassigned_patients_tree = ttk.Treeview(docpa_subwin, selectmode='browse', show='headings')

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
        assigned_patients_tree = ttk.Treeview(docpa_subwin, selectmode='browse', show='headings')

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
        # Count
        Label(docpa_subwin, text=f"COUNT: {assigned_patients_count}", anchor='e', bg='deep sky blue', fg='black', font=("Ariel", 16, 'bold')).place(x=fulwidth/4+50,y=fulheight-150,width=200,height=50)
        Label(docpa_subwin, text=f"COUNT: {unassigned_patients_count}", anchor='e',fg='black', font=("Ariel", 16, 'bold')).place(x=fulwidth/4*3+50,y=fulheight-150,width=200,height=50)

        # ===============================================================================
        # Buttons
        assign_patient_button = Button(docpa_subwin, text='ASSIGN PATIENT', font=("Ariel", 16, 'bold'), fg='white', bg='deep sky blue', relief='ridge',
            activebackground='dark blue', activeforeground='white', command=lambda: assign_patient(docpa_subwin, fulwidth, fulheight, unassigned_patients_tree, assigned_patients_tree, unassigned_patients_list, assigned_patients_list, patients_list, doctor_id, pa_doc_list))
        assign_patient_button.place(x=fulwidth/2+50, y=fulheight-150, width=250, height=50)

        unassign_patient_button = Button(docpa_subwin, text='UNASSIGN PATIENT', font=("Ariel", 16, 'bold'), fg='deep sky blue', relief='ridge',
            activebackground='dark blue', activeforeground='white', command=lambda: unassign_patient(docpa_subwin, fulwidth, fulheight, unassigned_patients_tree, assigned_patients_tree, unassigned_patients_list, assigned_patients_list, patients_list, doctor_id, pa_doc_list))
        unassign_patient_button.place(x=50, y=fulheight-150, width=250, height=50)

def assign_patient(docpa_subwin, fulwidth, fulheight, unassigned_patients_tree, assigned_patients_tree, unassigned_patients_list, assigned_patients_list, patients_list, doctor_id, pa_doc_list):
    if len(unassigned_patients_tree.selection())>0:
        selected_unassigned_patient = unassigned_patients_tree.selection()[0]
        patient_id = unassigned_patients_tree.item(selected_unassigned_patient, 'values')[0]

        pa_doc_list.append(Pa_Doc(patient_id, doctor_id))

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
        # ===============================================================================
        # Count
        Label(docpa_subwin, text=f"COUNT: {assigned_patients_count}", anchor='e', bg='deep sky blue', fg='black', font=("Ariel", 16, 'bold')).place(x=fulwidth/4+50,y=fulheight-150,width=200,height=50)
        Label(docpa_subwin, text=f"COUNT: {unassigned_patients_count}", anchor='e',fg='black', font=("Ariel", 16, 'bold')).place(x=fulwidth/4*3+50,y=fulheight-150,width=200,height=50)

def unassign_patient(docpa_subwin, fulwidth, fulheight, unassigned_patients_tree, assigned_patients_tree, unassigned_patients_list, assigned_patients_list, patients_list, doctor_id, pa_doc_list):
    if len(assigned_patients_tree.selection())>0:
        selected_assigned_patient = assigned_patients_tree.selection()[0]
        patient_id = assigned_patients_tree.item(selected_assigned_patient, 'values')[0]

        for relation in pa_doc_list:
            if relation.get_PatientID() == patient_id and relation.get_DoctorID() == doctor_id:
                pa_doc_list.remove(relation)
    
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
        # Count
        Label(docpa_subwin, text=f"COUNT: {assigned_patients_count}", anchor='e', bg='deep sky blue', fg='black', font=("Ariel", 16, 'bold')).place(x=fulwidth/4+50,y=fulheight-150,width=200,height=50)
        Label(docpa_subwin, text=f"COUNT: {unassigned_patients_count}", anchor='e',fg='black', font=("Ariel", 16, 'bold')).place(x=fulwidth/4*3+50,y=fulheight-150,width=200,height=50)

def doc_press(window, fulwidth, fulheight, doctors_list, patients_list, pa_doc_list):
    global selected_doctor
    selected_doctor = -1

    doc_subwin = Toplevel(window)
    doc_subwin.geometry("%dx%d" % (fulwidth, fulheight))
    icon = PhotoImage(file = "images/HIMS Icon.png")
    doc_subwin.iconphoto(False, icon)
    doc_subwin.title("Doctors Information Management")
    Frame(doc_subwin, bg='deep sky blue').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)
    
    assigned_patients_list = []
    unassigned_patients_list = []

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
    doc_tree = ttk.Treeview(doc_subwin, selectmode='browse', show='headings')

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
    doc_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_people_list_by_column(doc_tree, doctors_list, "ID", False))
    doc_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_people_list_by_column(doc_tree, doctors_list, "Name", False))
    doc_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_people_list_by_column(doc_tree, doctors_list, "Gender", False))
    doc_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_people_list_by_column(doc_tree, doctors_list, "Date of Birth", False))

    doc_tree.bind('<Motion>', 'break')
    
    # Insert Data
    for doctor in doctors_list:
        doc_tree.insert(parent='', index = 'end', iid=doctor.get_id(), text='', values=(doctor.get_id(), doctor.get_name(), doctor.get_gend(), doctor.get_dob()))
        
    doc_tree.place(x=fulwidth/2+50, y=50, height=fulheight-250, width=fulwidth/2-100)


    #=========================================================================================
    
    # Doctor Control
    Label(doc_subwin, bg='deep sky blue', fg='white', text='DOCTORS MANAGEMENT', font=("Ariel", 20, 'bold')).place(x=50, y=25, width=fulwidth/2-100, height=50)
    Frame(doc_subwin, bg='crimson').place(x=50, y=85, width=fulwidth/2-100, height=2)
    entry_frame = Frame(doc_subwin, bg='deep sky blue')
    entry_frame.place(x=50, y=100, width=fulwidth/2-100, height=fulheight/2)
    Frame(doc_subwin, bg='crimson').place(x=50, y=350, width=fulwidth/2-100, height=2)
    Label(doc_subwin, text='  - Entries marked with " * " must not be empty ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=360, height=30)
    Label(doc_subwin, text='  - ID must be " D-xxx " ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=385, height=30)
    Label(doc_subwin, text='  - Gender must be " M " or " F " ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=410, height=30)
    Label(doc_subwin, text='  - Date of Birth must be " dd/mm/yyyy " ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=435, height=30)
    Label(doc_subwin, text='  - Phone & Salary must be numbers ', anchor='w', bg='deep sky blue', fg='white', font=("Ariel", 12, 'bold')).place(x=50, y=460, height=30)


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
    add_doctor_button = Button(doc_subwin, text='ADD DOCTOR',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: doc_add(doctors_list, doc_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry,phone_entry,email_entry,dept_entry,salary_entry))
    add_doctor_button.place(x=50, y=fulheight-75-85-10-50, width=150, height=50)

    update_doctor_button = Button(doc_subwin, text='UPDATE',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: doc_update(doctors_list, pa_doc_list, doc_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry))
    update_doctor_button.place(x=fulwidth/2-50-150, y=fulheight-75-85-10-50, width=150, height=50)

    clear_button = Button(doc_subwin, text='CLEAR',anchor='center',font=("Ariel", 12,'bold'), fg='red', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(entry_frame, id_entry, name_entry, gend_entry, dob_entry,phone_entry,email_entry,dept_entry,salary_entry))
    clear_button.place(x=fulwidth/4*1-100, y=fulheight-75-85-10-50, width=200, height=50)

    remove_doctor_button = Button(doc_subwin, text='REMOVE SELECTED',anchor='center',font=("Ariel", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: doc_remove(doctors_list, doc_tree, pa_doc_list))
    remove_doctor_button.place(x=fulwidth/4*3-100, y=fulheight-75-85, width=200, height=50)

    remove_all_doctor_button = Button(doc_subwin, text='REMOVE ALL',anchor='center',font=("Ariel", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: all_doc_remove(doc_tree, doctors_list, pa_doc_list))
    remove_all_doctor_button.place(x=fulwidth-50-150, y=fulheight-75-85, width=150, height=50)

    select_doctor_button = Button(doc_subwin, text='SELECT',anchor='center',font=("Ariel", 12,'bold'), bg='deep sky blue',fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: doc_select(doctors_list, doc_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry,phone_entry,email_entry,dept_entry,salary_entry))
    select_doctor_button.place(x=fulwidth/2+50, y=fulheight-75-85, width=150, height=50)

    patients_assignment_button = Button(doc_subwin, text='PATIENTS ASSIGNMENT',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: patients_assignment(doc_subwin, doc_tree, fulwidth, fulheight, pa_doc_list, patients_list, assigned_patients_list, unassigned_patients_list))
    patients_assignment_button.place(x=50,y=fulheight-75-85, width=fulwidth/2-100, height=50)