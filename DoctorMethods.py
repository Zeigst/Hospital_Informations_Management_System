from domains.People import *
from tkinter import *
from tkinter import ttk
from tk import *
from PIL import ImageTk, Image



def doc_press(window, fulwidth, fulheight, doctors_list):
    subwin = Toplevel(window)
    subwin.geometry("%dx%d" % (fulwidth, fulheight))
    icon = PhotoImage(file = "images/HIMS Icon.png")
    subwin.iconphoto(False, icon)
    subwin.title("Doctors Information Management")
    Frame(subwin, bg='deep sky blue').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)


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
    #scroll_bar = ttk.Scrollbar(subwin, orient="vertical", command=doc_tree.yview)
    #scroll_bar.place(x=fulwidth/4*3+175, y=100, height=fulheight/2)
    #doc_tree.configure(yscrollcommand=scroll_bar.set)

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
    count = 0
    for doctor in doctors_list:
        doc_tree.insert(parent='', index = 'end', iid=count, text='', values=(doctor.get_id(), doctor.get_name(), doctor.get_gend(), doctor.get_dob()))
        count += 1
        
    doc_tree.place(x=fulwidth/2+50, y=50, height=fulheight-150, width=fulwidth/2-100)




