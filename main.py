# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
import sys
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox, ttk

is_unhappy_exist = True


def initialize_field(n):
    field = np.zeros((n, n))
    num_cells = n * n
    num_blue = int(0.45 * num_cells)
    num_red = int(0.45 * num_cells)
    num_empty = num_cells - num_blue - num_red
    colors = [0] * num_blue + [2] * num_red + [1] * num_empty
    random.shuffle(colors)
    for i in range(n):
        for j in range(n):
            field[i, j] = colors[i * n + j]
    print(field)
    return field


def is_unhappy(field, i, j):
    color = field[i, j]
    neighbors = get_neighbors(field, i, j)
    count_same_color = sum(1 for x in neighbors if x == color)
    return count_same_color < 2


def get_neighbors(field, i, j):
    n = len(field)
    lenth = n-1
    neighbors = []
    if i == 0 and j == 0:
        neighbors.append(field[0, 1])
        neighbors.append(field[1, 0])
        neighbors.append(field[1, 1])
        neighbors.append(field[0, lenth])
        neighbors.append(field[lenth, 0])
        neighbors.append(field[lenth, lenth])
    elif i == 0 and j == lenth:
        print(field)
        print("i= "+ str(i)+ "j= " + str(j)+": " + str(field[i,j]))
        neighbors.append(field[0, lenth-1])
        neighbors.append(field[1, lenth - 1])
        neighbors.append(field[1, lenth])
        neighbors.append(field[0, 0])
        neighbors.append(field[lenth, 0])
        neighbors.append(field[lenth, lenth])
    elif i == lenth and j == 0:
        neighbors.append(field[lenth-1, 0])
        neighbors.append(field[lenth-1, 1])
        neighbors.append(field[lenth, 1])
        neighbors.append(field[0, 0])
        neighbors.append(field[0, lenth])
        neighbors.append(field[lenth, lenth])
    elif i == lenth and j == lenth:
        neighbors.append(field[lenth - 1, lenth - 1])
        neighbors.append(field[lenth - 1, lenth])
        neighbors.append(field[lenth, lenth - 1])
        neighbors.append(field[0, 0])
        neighbors.append(field[0, lenth])
        neighbors.append(field[lenth, 0])
    else:
        for x in range(max(0, i - 1), min(i + 2, n)):
            for y in range(max(0, j - 1), min(j + 2, n)):
                if x != i or y != j:
                    neighbors.append(field[x, y])
    return neighbors


def move_unhappy_cell(field):
    n = len(field)
    unhappy_cells = []
    for i in range(n):
        for j in range(n):
            if field[i, j] != 1 and is_unhappy(field, i, j):
                unhappy_cells.append((i, j))
    if len(unhappy_cells) == 0:
        messagebox.showinfo(title="Информация", message="Нет несчастливых ячеек")
        global is_unhappy_exist
        is_unhappy_exist = False
        return  # Нет несчастливых ячеек
    print(unhappy_cells)
    cell = random.choice(unhappy_cells)
    print(cell)
    empty_cells = []
    for i in range(n):
        for j in range(n):
            if field[i, j] == 1:
                empty_cells.append((i, j))
    if len(empty_cells) == 0:
        print('Нет пустых ячеек')
        return  # Нет пустых ячеек
    new_cell = random.choice(empty_cells)
    field[new_cell[0], new_cell[1]] = field[cell[0], cell[1]]
    field[cell[0], cell[1]] = 1
    print(field)


def display_field(field):
    plt.imshow(field, cmap='coolwarm', interpolation='nearest', vmin=0, vmax=2)
    plt.colorbar(ticks=[0, 1, 2])
    plt.show()


def start_programm():
    n = int(entry1.get())  # Размер поля
    step = int(entry2.get())  # Шаг отображения результатов
    field = initialize_field(n)
    display_field(field)

    counter = 0
    while is_unhappy_exist:
        move_unhappy_cell(field)
        counter += 1
        if counter % step == 0:
            display_field(field)
    display_field(field)
    return


# Создание окна
root = Tk()
root.geometry("500x300")
root.resizable(False, False)
# Создание виджетов
label1 = ttk.Label(root, text="Введите размер поля клеток:", justify="left")
label1.pack(fill=BOTH, pady=5, padx=40)

entry1 = Entry(root)
entry1.pack(fill=BOTH, pady=5, padx=40)

label2 = ttk.Label(root, text="Введите шаг для отображения результатов:", justify="left")
label2.pack(fill=BOTH, pady=5, padx=40)

entry2 = Entry(root)
entry2.pack(fill=BOTH, pady=5, padx=40)

button = ttk.Button(text="Начать", command=start_programm)
button.pack(fill=BOTH, pady=10, padx=40)

# Запуск цикла обработки событий
root.mainloop()
