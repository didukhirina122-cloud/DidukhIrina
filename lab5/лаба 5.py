import math              # математичні функції (sqrt, sin, cos тощо)
import random            # генерація випадкових чисел
import requests           # робота з HTTP-запитами
import numpy as np        # бібліотека для наукових обчислень та масивів
import pandas as pd       # робота з таблицями та даними
import matplotlib.pyplot as plt  # створення графіків
import datetime           # робота з датами та часом
import json               # робота з JSON-даними
import os                 # взаємодія з файловою системою
import time               # функції, пов’язані з часом (затримки, вимірювання)

# 1 Використання бібліотеки math
try:
    number = 25                                  # створюємо змінну з числом
    print(f"Квадратний корінь з {number} = {math.sqrt(number)}")  # обчислення квадратного кореня
except Exception as e:
    print("Помилка в модулі math:", e)           # обробка помилки, якщо виникне

# 2 Використання бібліотеки random
try:
    rand_list = [random.randint(1, 100) for _ in range(5)]  # створюємо список із 5 випадкових чисел
    print("Список випадкових чисел:", rand_list)            # виводимо результат
except Exception as e:
    print("Помилка в модулі random:", e)                    # якщо виникла помилка

# 3 Використання бібліотеки numpy
try:
    arr = np.array([1, 2, 3, 4, 5])                    # створюємо масив NumPy
    print("Сума елементів масиву:", np.sum(arr))        # обчислюємо суму елементів
except Exception as e:
    print("Помилка в модулі numpy:", e)

# 4 Використання бібліотеки pandas
try:
    data = pd.DataFrame({                               # створюємо таблицю (DataFrame)
        "Name": ["Іра", "Олег", "Марія"],              # стовпець із іменами
        "Score": [95, 88, 92]                          # стовпець із балами
    })
    print("DataFrame з pandas:\n", data)                # виводимо таблицю
except Exception as e:
    print("Помилка в модулі pandas:", e)

# 5 Використання бібліотеки matplotlib
try:
    plt.plot([1, 2, 3], [2, 4, 1])                     # будуємо простий графік
    plt.title("Простий графік")                        # додаємо заголовок
    plt.xlabel("X")                                    # підпис осі X
    plt.ylabel("Y")                                    # підпис осі Y
    plt.savefig("plot.png")                            # зберігаємо графік у файл
    plt.close()                                        # закриваємо вікно графіка
    print("Графік збережено як plot.png")              # повідомлення користувачу
except Exception as e:
    print("Помилка в модулі matplotlib:", e)