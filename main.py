from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from domains.People import *
import DoctorMethods
import database

# doctors_list = []

def on_ready():
    global doctors_list
    doctors_list = database.load_data()

def on_close():
    global doctors_list
    database.save_doctor(doctors_list)
    window.destroy()

global doctors_list
doctors_list = []


#Create main window
window = Tk()

#Set title
window.title("Hospital Information Management System")
icon = PhotoImage(file = "images/HIMS Icon.png")
window.iconphoto(False, icon)

#Make full screen
fulwidth= window.winfo_screenwidth()
fulheight= window.winfo_screenheight()
window.geometry("%dx%d" % (fulwidth, fulheight))

#==========================================================================================
# Decorate Main Menu
with Image.open("images/Hospital.png") as img:
    resized_image = img.resize((250, 250))
    HospitalImg = ImageTk.PhotoImage(resized_image)

with Image.open("images/Heart.png") as img:
    resized_image = img.resize((150, 150))
    HeartImg = ImageTk.PhotoImage(resized_image)

# Left Panel
Frame(window, bg="deep sky blue").place(x = fulwidth/2, y = 0, width = fulwidth/2, height = fulheight)
Frame(window, bg="crimson").place(x = 24, y = 24, width = fulwidth/2-48, height = fulheight-98)
Frame(window, bg="white").place(x = 26, y = 26, width = fulwidth/2-52, height = fulheight-102)
Frame(window, bg="light grey").place(x = 50, y = 50, width = fulwidth/2-100, height = fulheight-150)
Label(window, image=HeartImg, bg="light grey", anchor='center').place(x = (fulwidth/4)-75, y=(fulheight/11), width=150, height=150)

# Right Panel
Label(window, text="HOSPITAL INFORMATION",bg="deep sky blue", fg="white", font=("Ariel", 25,'bold')).place(x = fulwidth/2, y = fulheight-250, width=fulwidth/2, height=25)
Label(window, text="MANAGEMENT SYSTEM",bg="deep sky blue", fg="white", font=("Ariel", 25,'bold')).place(x = fulwidth/2, y = fulheight-200, width=fulwidth/2, height=25)
Label(window, image=HospitalImg, bg="deep sky blue", anchor='center').place(x = (fulwidth/8)*6-125, y=(fulheight/7), width=250, height=250)


# Buttons
Button(window, text="DOCTORS", anchor='center', font=("Ariel", 20,'bold'), bg="deep sky blue", fg="white", relief='ridge', 
            activebackground='dark blue', activeforeground='white', command=lambda: DoctorMethods.doc_press(window, fulwidth, fulheight, doctors_list)).place(x=100, y=fulheight/2-100, width=fulwidth/2-200, height = 50)

Button(window, text="WORKERS", anchor='center', font=("Ariel", 20,'bold'), bg="deep sky blue", fg="white", relief='ridge', 
            activebackground='dark blue', activeforeground='white').place(x=100, y=fulheight/2-40, width=fulwidth/2-200, height = 50)

Button(window, text="PATIENTS", anchor='center', font=("Ariel", 20,'bold'), bg="deep sky blue", fg="white", relief='ridge', 
            activebackground='dark blue', activeforeground='white').place(x=100, y=fulheight/2+20, width=fulwidth/2-200, height = 50)

Button(window, text="MEDICINES", anchor='center', font=("Ariel", 20,'bold'), bg="deep sky blue", fg="white", relief='ridge', 
            activebackground='dark blue', activeforeground='white').place(x=100, y=fulheight/2+80, width=fulwidth/2-200, height = 50)

Button(window, text="EXIT", anchor='center', font=("Ariel", 20,'bold'), bg="deep sky blue", fg="white", relief='ridge', 
            activebackground='dark blue', activeforeground='white').place(x=100, y=fulheight/2+140, width=fulwidth/2-200, height = 50)


def main():
    on_ready()
    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()

if __name__ == "__main__":
    main()