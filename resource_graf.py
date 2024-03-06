import sqlite3
import matplotlib.pyplot as plt

meat_data = []
cerial_data = []
wheat_data = []


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('journal', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_number(self):
        global meat_data
        global cerial_data
        global wheat_data
        self.cursor.execute("select count(*) from eat")
        row_count = self.cursor.fetchone()
        row_count = int(row_count[0])
        self.cursor.execute("SELECT * FROM eat")
        al = self.cursor.fetchall()
        for i in range(row_count):
            a = al[i]
            meat_data.append(a[1])
            cerial_data.append(a[2])
            wheat_data.append(a[3])

# Создаем экземпляр класса Database
db = Database()
db.get_number()

# Создаем график после загрузки данных
plt.figure(figsize=(10, 5))
plt.plot(meat_data, label='Мясо', marker='o')
plt.plot(cerial_data, label='Крупы', marker='o')
plt.plot(wheat_data, label='Колосья, сено и тд', marker='o')
plt.xlabel('Дни')
plt.ylabel('Значения')
plt.title('График температуры и осадков')
plt.legend()
plt.grid(True)
plt.show()