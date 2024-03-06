from tkinter import *
import sqlite3


root = Tk()


# Начало блока 5
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('journal', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def register(self, temp, ocad):
        self.cursor.execute(f'INSERT INTO journaltos (temp, ocad) VALUES (?, ?)', (temp, ocad))
        self.conn.commit()
        root.destroy()
        return True
# Конец блока 5


db = Database()


def add():
    temp = text.get(1.0, END)
    ocad = text2.get(1.0, END)
    db.register(temp, ocad)


root.title("Журнал исследовательской станции")
icon = PhotoImage(file="media\icon.png")
root.iconphoto(False, icon)
root.geometry(f'400x200')
lbl = Label(root, text='Температура')
lbl.pack(anchor='nw')
text = Text(width=5, height=1)
text.pack(anchor='nw')
lbl1 = Label(root, text='Осадки')
lbl1.pack(anchor='nw')
text2 = Text(width=5, height=1)
text2.pack(anchor='nw')
button = Button(root, text="ввод данных о погоде за день", command=add, width=30, height=1)
button.pack(anchor="nw", padx=0, pady=0)

root.mainloop()

