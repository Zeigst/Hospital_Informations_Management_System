from domains.People import *
from tkinter import *
from tkinter import ttk
from tk import *
from PIL import ImageTk, Image
import utils

def clear_entry(input_entry, input_id, input_name, input_gend, input_dob):
    # Delete all Warnings
    Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='                               ', font=("Ariel", 14, 'bold')).grid(column=3,row=0, sticky='w')
    Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='                ', font=("Ariel", 14, 'bold')).grid(column=3,row=1, sticky='w')
    Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='                ', font=("Ariel", 14, 'bold')).grid(column=3,row=2, sticky='w')
    Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='                ', font=("Ariel", 14, 'bold')).grid(column=3,row=3, sticky='w')
    
    # Empty Entry boxes
    input_id.delete(0, END)
    input_name.delete(0, END)
    input_gend.delete(0, END)
    input_dob.delete(0, END)
    
def doc_add(doctors_list, doc_tree, doc_count, input_entry, input_id, input_name, input_gend, input_dob):
    # Delete all Warnings
    Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='                                          ', font=("Ariel", 14, 'bold')).grid(column=3,row=0, sticky='w')
    Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='                       ', font=("Ariel", 14, 'bold')).grid(column=3,row=1, sticky='w')
    Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='                       ', font=("Ariel", 14, 'bold')).grid(column=3,row=2, sticky='w')
    Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='                       ', font=("Ariel", 14, 'bold')).grid(column=3,row=3, sticky='w')

    id = input_id.get()
    name = input_name.get()
    gend = input_gend.get()
    dob = input_dob.get()

    # Validation
    valid_check = 0
    #Validate ID
    if len(id) == 0:
        Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=3,row=0, sticky='w')
        valid_check += 1
    elif utils.invalid_id(id, "D-") == 1:
        Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=3,row=0, sticky='w')
        valid_check += 1
    else:
        for doctor in doctors_list:
            if doctor.get_id() == id:
                Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='ID already exist', font=("Ariel", 14, 'bold')).grid(column=3,row=0, sticky='w')
                valid_check += 1
                break
    
    # Validate Name
    if len(name) == 0:
        Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=3,row=1, sticky='w')
        valid_check += 1

    # Validate Gender
    if len(gend) == 0:
        Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=3,row=2, sticky='w')
        valid_check += 1
    elif utils.invalid_gend(gend) == 1:
        Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=3,row=2, sticky='w')
        valid_check += 1

    # Validate Date of Birth
    if len(dob) == 0:
        Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='EMPTY', font=("Ariel", 14, 'bold')).grid(column=3,row=3, sticky='w')
        valid_check += 1
    elif utils.invalid_dob(dob) == 1:
        Label(input_entry,anchor='w', bg='deep sky blue', fg='crimson', text='INVALID', font=("Ariel", 14, 'bold')).grid(column=3,row=3, sticky='w')
        valid_check += 1
    
    # If All Valid
    if valid_check == 0:
        # Add to doctors_list
        doctors_list.append(Doctor(id, name, gend, dob))
        # Display on Treeview
        doc_tree.insert(parent='', index = 'end', iid=doc_count, text='', values=(id, name, gend, dob))
        doc_count += 1

        # Empty Entry boxes
        input_id.delete(0, END)
        input_name.delete(0, END)
        input_gend.delete(0, END)
        input_dob.delete(0, END)


def doc_press(window, fulwidth, fulheight, doctors_list):
    subwin = Toplevel(window)
    subwin.geometry("%dx%d" % (fulwidth, fulheight))
    icon = PhotoImage(file = "images/HIMS Icon.png")
    subwin.iconphoto(False, icon)
    subwin.title("Doctors Information Management")
    Frame(subwin, bg='deep sky blue').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)
    Frame(subwin, bg='white').place(x=24, y=24 ,width=fulwidth/2-48, height=fulheight/2-98)
    Frame(subwin, bg='deep sky blue').place(x=26, y=26 ,width=fulwidth/2-52, height=fulheight/2-102)
    input_entry = Frame(subwin, bg='deep sky blue')
    input_entry.place(x=50, y=50, width=fulwidth/2-100, height=fulheight/2-150)
    Frame(subwin, bg='crimson').place(x=50, y=175 ,width=fulwidth/2-100, height=2)


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
    doc_tree = ttk.Treeview(subwin, selectmode='browse')

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
    doc_tree.heading("ID", text="ID", anchor='center')
    doc_tree.heading("Name", text="Name", anchor='center')
    doc_tree.heading("Gender", text="Gender", anchor='center')
    doc_tree.heading("Date of Birth", text="Date of Birth", anchor='center')

    doc_tree.bind('<Motion>', 'break')
    # Insert Data
    doc_count = 0
    for doctor in doctors_list:
        doc_tree.insert(parent='', index = 'end', iid=doc_count, text='', values=(doctor.get_id(), doctor.get_name(), doctor.get_gend(), doctor.get_dob()))
        doc_count += 1
        
    doc_tree.place(x=fulwidth/2+50, y=50, height=fulheight-150, width=fulwidth/2-100)


    #=========================================================================================
    # Add doctor
    # Label
    Label(input_entry,anchor='w', bg='deep sky blue', fg='white', text='ID: ', font=("Ariel", 14, 'bold')).grid(column=0,row=0, sticky='w')
    Label(input_entry,anchor='w', bg='deep sky blue', fg='white', text='Name: ', font=("Ariel", 14, 'bold')).grid(column=0,row=1,sticky='w')
    Label(input_entry,anchor='w', bg='deep sky blue', fg='white', text='Gender: ', font=("Ariel", 14, 'bold')).grid(column=0,row=2,sticky='w')
    Label(input_entry,anchor='w', bg='deep sky blue', fg='white', text='DoB: ', font=("Ariel", 14, 'bold')).grid(column=0,row=3,sticky='w')

    Label(input_entry,anchor='w', bg='deep sky blue', fg='white', text='( D-xxx )', font=("Ariel", 14, 'bold')).grid(column=2,row=0, sticky='w')
    Label(input_entry,anchor='w', bg='deep sky blue', fg='white', text='( M/F )', font=("Ariel", 14, 'bold')).grid(column=2,row=2, sticky='w')
    Label(input_entry,anchor='w', bg='deep sky blue', fg='white', text='( dd/mm/yyyy )', font=("Ariel", 14, 'bold')).grid(column=2,row=3, sticky='w')
    # Entry
    input_id = Entry(input_entry)
    input_id.grid(column=1,row=0,sticky='e')

    input_name = Entry(input_entry)
    input_name.grid(column=1,row=1,sticky='e')

    input_gend = Entry(input_entry)
    input_gend.grid(column=1,row=2,sticky='e')

    input_dob = Entry(input_entry)
    input_dob.grid(column=1,row=3,sticky='e')

    # Buttons
    add_doctor = Button(subwin, text='ADD DOCTOR',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: doc_add(doctors_list, doc_tree, doc_count, input_entry, input_id, input_name, input_gend, input_dob))
    add_doctor.place(x=50, y=200, width=150, height=50)

    clear = Button(subwin, text='CLEAR',anchor='center',font=("Ariel", 12,'bold'), fg='deep sky blue', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(input_entry, input_id, input_name, input_gend, input_dob))
    clear.place(x=225, y=200, width=150, height=50)