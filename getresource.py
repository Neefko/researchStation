from tkinter import *
import sqlite3


# Начало блока 7
root = Tk()
temper = 0
ocad = 0
items = []

wheat = 0
meat = 0
cereal = 0


# Начало блока 5 и 6
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('journal', check_same_thread=False)
        self.cursor = self.conn.cursor()


class Database1(Database):
    def get_noeat(self):
        global temper
        global ocad
        self.cursor.execute("select count(*) from noeat")
        row_count = self.cursor.fetchone()
        row_count = int(row_count[0])
        self.cursor.execute("SELECT * FROM noeat")
        al = self.cursor.fetchall()
        for i in range(row_count):
            a = al[i]
            temper += a[1]
            b = al[i]
            ocad += b[2]


class Database2(Database):
    def eat(self):
        global wheat
        global meat
        global cereal
        self.cursor.execute("select count(*) from eat")
        row_count = self.cursor.fetchone()
        row_count = int(row_count[0])
        self.cursor.execute("SELECT * FROM eat")
        al = self.cursor.fetchall()
        for i in range(row_count):
            a = al[i]
            meat += a[1]
            b = al[i]
            cereal += b[2]
            c = al[i]
            wheat += c[3]
# Конец блока 5 и 6


db1 = Database1()
db2 = Database2()

db1.get_noeat()
db2.eat()
temper = str(temper) + ' л'
ocad = str(ocad) + ' кг'

meat = str(meat) + ' кг'
cereal = str(cereal) + ' кг'
wheat = str(wheat) + ' кг'


root.title("Анализ журнала исследовательской станции")
icon = PhotoImage(file="media\icon.png")
root.iconphoto(False, icon)
root.geometry(f'300x400')
l2 = Label(root, text='Непищевые продукты')
l2.pack(anchor='nw')
lbl = Label(root, text='Литров воды')
lbl.pack(anchor='nw')
lbl_number2 = Label(root, text=temper)
lbl_number2.pack(anchor='nw')
lbl1 = Label(root, text='Кг древесины')
lbl1.pack(anchor='nw')
lbl_number1 = Label(root, text=ocad)
lbl_number1.pack(anchor='nw')

l1 = Label(root, text='Пищевые продукты')
l1.pack(anchor='nw')
lbl9 = Label(root, text='Кг мяса')
lbl9.pack(anchor='nw')
lbl_number9 = Label(root, text=meat)
lbl_number9.pack(anchor='nw')
lbl9 = Label(root, text='Кг крупы')
lbl9.pack(anchor='nw')
lbl_number19 = Label(root, text=cereal)
lbl_number19.pack(anchor='nw')
lbl92 = Label(root, text='Кг Колосьев, сена и тд')
lbl92.pack(anchor='nw')
lbl_number192 = Label(root, text=wheat)
lbl_number192.pack(anchor='nw')
# Конец блока 7

root.mainloop()
