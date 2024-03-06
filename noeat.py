from tkinter import *
import sqlite3


root = Tk()


# Начало блока 5
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('journal', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def register(self, water, wood):
        self.cursor.execute(f'INSERT INTO noeat (water, wood) VALUES (?, ?)', (water, wood))
        self.conn.commit()
        root.destroy()
        return True
# Конец блока 5


db = Database()


def add():
    wood = text.get(1.0, END)
    water = text2.get(1.0, END)
    db.register(water, wood)


root.title("Ресурсы исследовательской станции")
icon = PhotoImage(file="media\icon.png")
root.iconphoto(False, icon)
root.geometry(f'400x200')
lb = Label(root, text='Если нет то 0, если забираете то минус и количество')
lb.pack(anchor='nw')
lbl = Label(root, text='Вода')
lbl.pack(anchor='nw')
text = Text(width=5, height=1)
text.pack(anchor='nw')
lbl1 = Label(root, text='Дерево')
lbl1.pack(anchor='nw')
text2 = Text(width=5, height=1)
text2.pack(anchor='nw')
button = Button(root, text="Ввод данных", command=add)
button.pack(anchor="nw", padx=0, pady=0)

root.mainloop()