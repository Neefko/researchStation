from tkinter import *
import os


root = Tk()



def add():
    os.system('python noeat.py')
    root.destroy()


def add_eat():
    os.system('python eat.py')
    root.destroy()


root.title("Журнал исследовательской станции")
icon = PhotoImage(file="media\icon.png")
root.iconphoto(False, icon)
root.geometry(f'400x200')
button = Button(root, text="Еда", command=add_eat, width=30, height=1)
button.pack(anchor="nw", padx=0, pady=0)
button1 = Button(root, text="Не еда", command=add, width=30, height=1)
button1.pack(anchor="nw", padx=0, pady=0)

root.mainloop()

