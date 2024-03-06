from tkinter import *
import sqlite3
from functools import reduce


root = Tk()
temper = 0
ocad = 0
items = []


# Начало блока 5
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('journal', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_number(self):
        global temper
        global ocad
        self.cursor.execute("select count(*) from journaltos")
        row_count = self.cursor.fetchone()
        row_count = int(row_count[0])
        self.cursor.execute("SELECT * FROM journaltos")
        al = self.cursor.fetchall()
        for i in range(row_count):
            a = al[i]
            temper += a[1]
            b = al[i]
            items.append(b[2])
        # Начало блока 4
        if items:
            ocad = reduce(lambda x, y: x + y, items, 0)  # Добавляем начальное значение 0 для суммы
        # Конец блока 4
        if temper != 0:
            temper /= row_count
        else:
            temper = 0
# Конец блока 5


db = Database()
db.get_number()

temper = str(temper) + ' Градусов'
ocad = str(ocad) + ' мм'


root.title("Анализ журнала исследовательской станции")
icon = PhotoImage(file="media\icon.png")
root.iconphoto(False, icon)
root.geometry(f'400x200')
lbl = Label(root, text='Средняя температура')
lbl.pack(anchor='nw')
lbl_number2 = Label(root, text=temper)
lbl_number2.pack(anchor='nw')
lbl1 = Label(root, text='Общее кол-во осадков')
lbl1.pack(anchor='nw')
lbl_number1 = Label(root, text=ocad)
lbl_number1.pack(anchor='nw')

root.mainloop()
