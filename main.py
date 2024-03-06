from tkinter import *
from PIL import Image, ImageTk
import os
import sqlite3


# Начало блока 9
# Начало блока 5
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('journal', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def count(self):
        self.cursor.execute("select count(*) from journaltos")
        row_count = self.cursor.fetchone()
        return row_count
# Конец блока 5


db = Database()
root = Tk()
number = 0
photo_list = [
    ImageTk.PhotoImage(Image.open("media/lunaw.png")),
    ImageTk.PhotoImage(Image.open("media/lunab.png"))
]


# Функция смены темы/начало
def change_theme():
    current_bg = root.cget("bg")
    if current_bg == "white":
        root.configure(bg="black")
        theme_button.config(image=photo_list[1])
    elif current_bg == 'black':
        root.configure(bg="white")
        theme_button.config(image=photo_list[0])
# Функция смены темы/конец


def journal():
    global number
    number += 1
    os.system('python journal.py')


def weather():
    os.system('python weather.py')


def analysis():
    a = db.count()
    if a != 0:
        os.system('python analysis.py')


def add_resource():
    os.system('python resource.py')


def resource():
    os.system('python resource_graf.py')


def get_resource():
    os.system('python getresource.py')
# Функция смены темы/конец


# Создание окна/начало
root.title("Исследовательская станция на необитаемом острове")
icon = PhotoImage(file="media\icon.png")
root.iconphoto(False, icon)
w = root.winfo_screenwidth() // 2 - 350
h = root.winfo_screenheight() // 2 - 200
root.geometry(f'700x400+{w}+{h}')
root.minsize(700, 400)
root.maxsize(700, 400)
root.configure(bg="white")
theme_button = Button(root, text="Тема", command=change_theme, image=photo_list[0])
theme_button.grid(row=0, column=4, padx=150, pady=10, sticky=N+E)
# Создание окна/конец
# Начало блока 1
button = Button(root, text="ввод данных о погоде за день", command=journal, width=30, height=1)
button.grid(row=0, column=0, padx=10, pady=10, sticky=N+E)
# Конец блока 1
# Начало блока 2
button2 = Button(root, text="анализ данных о погоде")
button2.config(command=analysis)
button2.grid(row=0, column=1, padx=10, pady=10, sticky=N)

# Конец блока 2
# Начало блока 3

button3 = Button(root, text="Добавить ресурсы", width=30)
button3.config(command=add_resource)
button3.grid(row=1, column=0, padx=10, pady=10, sticky=N+W)
# Конец блока 3
# Начало блока 7
button4 = Button(root, text="Кол-во ресурсов", width=30)
button4.config(command=get_resource)
button4.grid(row=1, column=1, padx=10, pady=10, sticky=N+W)
# Конец блока 7
# Конец блока 9
# Начало блока 10
button5 = Button(root, text="График погоды", width=30, command=weather)
button5.grid(row=2, column=0, padx=10, pady=10, sticky=N+W)
button6 = Button(root, text="График ресурсов", width=30, command=resource)
button6.grid(row=2, column=1, padx=10, pady=10, sticky=N+W)
# Конец блока 10

root.mainloop()

