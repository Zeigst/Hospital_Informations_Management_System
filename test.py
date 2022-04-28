from tkinter import *
from tkinter import ttk

def show_selected():
    print(tv.selection())

ws = Tk()
ws.title('PythonGuides')

tv = ttk.Treeview(
    ws, 
    columns=(1, 2, 3), 
    show='headings', 
    height=3
    )
tv.pack()

tv.heading(1, text='roll number')
tv.heading(2, text='name')
tv.heading(3, text='class')

tv.insert(parent='', index=0, iid=0, values=(21, "Krishna", 5))
tv.insert(parent='', index=1, iid=1, values=(18, "Bhem", 3))
tv.insert(parent='', index=2, iid=2, values=(12, "Golu", 6))
tv.insert(parent='', index=3, iid=3, values=(6, "amul", 3))
tv.insert(parent='', index=4, iid=4, values=(12, "nestle", 6))
tv.insert(parent='', index=5, iid=5, values=(6, "zebronics", 3))

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")


Button(ws, text="Show Selected", command=show_selected).pack()

ws.mainloop()