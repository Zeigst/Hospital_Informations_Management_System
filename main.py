import tkinter as tk
from tk import *
import tkinter.messagebox as msb

#Create main window
window = tk.Tk()

#Set title
window.title("Hospital Information Management System")

#Make full screen
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

#Border
tk.Frame(window, bg="sky blue").place(x = 0, y = 0, width = width, height = 50)
tk.Frame(window, bg="sky blue").place(x = 0, y = height - 100, width = width, height = 50)
tk.Frame(window, bg="sky blue").place(x = 0, y = 0, width = 50, height = height)
tk.Frame(window, bg="sky blue").place(x = width-50, y = 0, width = 50, height = height)

#Lable
tk.Label(window, text="HOSPITAL INFORMATION MANAGEMENT SYSTEM", font=("Ariel", 25)).place(x = 50, y = 50,)



def main():
    window.mainloop()

if __name__ == "__main__":
    main()