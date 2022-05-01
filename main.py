from tkinter import *
from PIL import ImageTk, Image
from domains.People import *
import methods.DoctorMethods as DoctorMethods
import methods.PatientMethods as PatientMethods
import methods.MedicineMethods as MedicineMethods
import methods.WorkerMethods as WorkerMethods
import credits
import database

def on_ready():
    database.unzip_data()
    global doctors_list
    doctors_list = database.load_doctors()
    global workers_list
    workers_list = database.load_workers()
    global patients_list
    patients_list = database.load_patients()
    global medicines_list
    medicines_list = database.load_medicines()
    global pa_doc_list
    pa_doc_list = database.load_pa_doc()
    global pa_med_list
    pa_med_list = database.load_pa_med()

def on_close():
    global doctors_list
    database.save_doctors(doctors_list)
    global workers_list
    database.save_workers(workers_list)
    global patients_list
    database.save_patients(patients_list)
    global medicines_list
    database.save_medicines(medicines_list)
    global pa_doc_list
    database.save_pa_doc(pa_doc_list)
    global pa_med_list
    database.save_pa_med(pa_med_list)
    database.zip_data()
    window.destroy()

global doctors_list
doctors_list = []
global workers_list
workers_list = []
global patients_list
patients_list = []
global medicines_list
medicines_list = []
global pa_doc_list
pa_doc_list = []
global pa_med_list
pa_med_list = []

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
doctors_button = Button(window, text="DOCTORS", anchor='center', font=("Ariel", 20,'bold'), bg="deep sky blue", fg="white", relief='ridge', 
            activebackground='dark blue', activeforeground='white', command=lambda: DoctorMethods.doc_press(window, fulwidth, fulheight, doctors_list, patients_list, pa_doc_list))
doctors_button.place(x=100, y=fulheight/2-100, width=fulwidth/2-200, height = 50)

workers_button = Button(window, text="WORKERS", anchor='center', font=("Ariel", 20,'bold'), bg="deep sky blue", fg="white", relief='ridge', 
            activebackground='dark blue', activeforeground='white', command=lambda: WorkerMethods.wor_press(window, fulwidth, fulheight, workers_list))
workers_button.place(x=100, y=fulheight/2-40, width=fulwidth/2-200, height = 50)

patients_button = Button(window, text="PATIENTS", anchor='center', font=("Ariel", 20,'bold'), bg="deep sky blue", fg="white", relief='ridge', 
            activebackground='dark blue', activeforeground='white', command=lambda: PatientMethods.pat_press(window, fulwidth, fulheight, doctors_list, patients_list, medicines_list, pa_doc_list, pa_med_list))
patients_button.place(x=100, y=fulheight/2+20, width=fulwidth/2-200, height = 50)

medicines_button = Button(window, text="MEDICINES", anchor='center', font=("Ariel", 20,'bold'), bg="deep sky blue", fg="white", relief='ridge', 
            activebackground='dark blue', activeforeground='white', command=lambda: MedicineMethods.med_press(window, fulwidth, fulheight, medicines_list, patients_list, pa_med_list))
medicines_button.place(x=100, y=fulheight/2+80, width=fulwidth/2-200, height = 50)

credit_button = Button(window, text="CREDITS", anchor='center', font=("Ariel", 20,'bold'), bg="deep sky blue", fg="white", relief='ridge', 
            activebackground='dark blue', activeforeground='white', command=lambda: credits.credits_press(window, fulwidth, fulheight))
credit_button.place(x=100, y=fulheight/2+140, width=fulwidth/2-200, height = 50)


def main():
    on_ready()
    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()

if __name__ == "__main__":
    main()