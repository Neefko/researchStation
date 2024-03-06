import sqlite3
from tkinter import *
import matplotlib.pyplot as plt

temperature_data = []
precipitation_data = []


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('journal', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_number(self):
        global temperature_data
        global precipitation_data
        self.cursor.execute("select count(*) from journaltos")
        row_count = self.cursor.fetchone()
        row_count = int(row_count[0])
        self.cursor.execute("SELECT * FROM journaltos")
        al = self.cursor.fetchall()
        for i in range(row_count):
            a = al[i]
            temperature_data.append(int(a[1]))
            precipitation_data.append(int(a[2]))


# Создаем экземпляр класса Database
db = Database()
db.get_number()

# Создаем график после загрузки данных
plt.figure(figsize=(10, 5))
plt.plot(temperature_data, label='Температура', marker='o')
plt.plot(precipitation_data, label='Осадки', marker='x')
plt.xlabel('Дни')
plt.ylabel('Значения')
plt.title('График температуры и осадков')
plt.legend()
plt.grid(True)
plt.show()