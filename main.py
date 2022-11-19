from operator import length_hint
import sys
import numpy as np
import random
import time
import threading
import dearpygui.dearpygui as dpg
from Patient import Patient

hospital = np.random.randint(3, size=(20, 25))

cnt = 0
hospital[0][0] = 3
hospital[19][0] = 3
hospital[0][24] = 3
hospital[19][24] = 3

hospital[10][11] = 5
hospital[10][13] = 5

for i in range(1, 19):
    a = random.randint(3, 4)
    if a == 4 and cnt <= 1 and hospital[i - 1][0] != 4 and hospital[i - 2][0] != 4 and hospital[i][1] != 2:
        cnt = cnt + 1
        hospital[i][0] = a
    else:
        hospital[i][0] = 3
    a = random.randint(3, 4)
    if a == 4 and cnt <= 1 and hospital[i - 1][24] != 4 and hospital[i - 2][24] != 4 and hospital[i][23] != 2:
        cnt = cnt + 1
        hospital[i][24] = a
    else:
        hospital[i][24] = 3
cnt = 0
for j in range(1, 24):
    a = random.randint(3, 4)
    if a == 4 and cnt <= 1 and hospital[19][j - 1] != 4 and hospital[19][j - 2] != 4 and hospital[18][j] != 2:
        cnt = cnt + 1
        hospital[19][j] = a
    else:
        hospital[19][j] = 3
    a = random.randint(3, 4)
    if a == 4 and cnt <= 1 and hospital[0][j - 1] != 4 and hospital[0][j - 2] != 4 and hospital[1][j] != 2:
        cnt = cnt + 1
        hospital[0][j] = a
    else:
        hospital[0][j] = 3
for i in range(0, 20):
    for j in range(0, 25):
        print(hospital[i][j], end=" ")
    print("\n")

dpg.create_context()
dpg.create_viewport(title="Escape")
#
# dpg.window(title="Lobby")
# dpg.add_button(label="Start", callback=open_main_win)

dpg.configure_viewport(0, x_pos=0, y_pos=0, width=1000, height=790)

m = 20
n = 25
path = np.zeros((m + 1, n + 1), dtype=int)
coord1 = [1, 0, -1, 0]
coord2 = [0, 1, 0, -1]
x = []
y = []

x1 = [0] * 150
y1 = [0] * 150

x2 = []
y2 = []

path2 = np.zeros((m + 1, n + 1), dtype=int)

with dpg.window(label="Mental hospital", width=900, height=700):
    with dpg.table(header_row=False) as table_id:

        for i in range(0, 26):
            dpg.add_table_column()

        for i in range(0, 20):
            with dpg.table_row(height=30):
                for j in range(0, 25):
                    with dpg.table_cell():

                        if hospital[i][j] == 0 or hospital[i][j] == 1:
                            dpg.highlight_table_cell(table_id, i, j, [173, 216, 230])
                        elif hospital[i][j] == 10:
                            dpg.highlight_table_cell(table_id, i, j, [200, 100, 45])
                        elif hospital[i][j] == 4:
                            dpg.highlight_table_cell(table_id, i, j, [85, 187, 51])
                            dpg.add_text("EXIT")
                        elif hospital[i][j] == 3 or hospital[i][j] == 2:
                            dpg.highlight_table_cell(table_id, i, j, [66, 73, 82])

dpg.highlight_table_cell(table_id, 10, 12, [100, 21, 199])
dpg.highlight_table_cell(table_id, 10, 11, [56, 48, 67])


def show():
    for i in range(m):
        for j in range(n):
            print(path[i][j], end=' ')
        print('\n')
    print('\n')


minim = 1000
counter = 0


def valid(ii, jj, steps):
    global minim
    if ii < 0 or ii > m - 1 or jj < 0 or jj > n - 1: return False
    if hospital[ii][jj] == 2 or hospital[ii][jj] == 3: return False
    if steps > minim: return False
    if path[ii][jj] != 0: return False
    return True


def backtracking(i, j, pas, steps):
    global minim
    global counter
    for k in range(4):
        ii = i + coord1[k]
        jj = j + coord2[k]

        x.append(ii)
        y.append(jj)

        steps = steps + 1

        if valid(ii, jj, steps) == 1:

            path[ii][jj] = pas + 1
            if hospital[ii][jj] == 4:
                if counter == 0:
                    counter = 1
                    for i in range(2, len(x)):
                        x2.append(x[i])
                        y2.append(y[i])

                if steps < minim:
                    minim = steps

                    for i in range(len(x)):
                        x1[i] = x[i]
                        y1[i] = y[i]

                    for i in range(len(x), len(x1)):
                        x1[i] = 25
                        y1[i] = 20

                    print(steps)

            backtracking(ii, jj, pas + 1, steps)
            path[ii][jj] = 0

        x.pop(len(x) - 1)
        y.pop(len(y) - 1)
        steps = steps - 1


print('\n')
path[10][11] = 1
for i in range(m):
    for j in range(n):
        print(path[i][j], end=' ')
    print('\n')
cnt = 0
backtracking(10, 11, 1, 0)
for i in range(len(x)):
    print(x[i], end=' ')

i = 10
j = 12
last_x = 10
last_y = 12

illnesses = ["Schizofrenie", "Parkinson", "Tulburare bipolara", "Alzheimer"]
patient_you = Patient("Andreea", 17, 27, "Alzheimer")
counter = 0


def schizo():
    global counter
    if counter % 5 == 0 and random.randrange(0, 2) == 1:
        print("Stop")
        with dpg.window(label="Delete Files", modal=True, show=True, tag="modal_id", no_title_bar=True):
            dpg.add_text("Ai un episod schizofrenic!")
            time.sleep(3)
            dpg.delete_item("modal_id")

def alz():
    global i, j, last_x, last_y
    aux_x = i
    aux_y = j
    if random.randrange(0, 3) != 0:
        dpg.highlight_table_cell(table_id, i, j, [173, 216, 230])
        i = last_x
        j = last_y
        dpg.highlight_table_cell(table_id, i, j, [100, 21, 199])
    last_x = aux_x
    last_y = aux_y



def move_player(sender, app_data):
    global i, j, counter, last_x, last_y
    counter = counter + 1
    if patient_you.get_illness() == "Schizofrenie":
        schizo()
    if patient_you.get_illness() == "Parkinson":
        time.sleep(0.7)
    if (counter % 6 == 0 or counter % 6 - 1 == 0) and patient_you.get_illness() == "Tulburare bipolara":
        if app_data == 39:
            app_data = app_data - 1
        else:
            app_data = app_data + 1

    if counter % 3 == 0 and patient_you.get_illness() == "Alzheimer":
        alz()

    if (app_data == 37 or app_data == 65) and hospital[i][j - 1] != 2 and hospital[i][j - 1] != 3:
        # VEST
        dpg.highlight_table_cell(table_id, i, j, [173, 216, 230])
        j = j - 1
        dpg.highlight_table_cell(table_id, i, j, [100, 21, 199])

    if (app_data == 38 or app_data == 87) and hospital[i - 1][j] != 2 and hospital[i - 1][j] != 3:
        # NORD
        dpg.highlight_table_cell(table_id, i, j, [173, 216, 230])
        i = i - 1
        dpg.highlight_table_cell(table_id, i, j, [100, 21, 199])

    if (app_data == 39 or app_data == 68) and hospital[i][j + 1] != 2 and hospital[i][j + 1] != 3:
        # EST
        dpg.highlight_table_cell(table_id, i, j, [173, 216, 230])
        j = j + 1
        dpg.highlight_table_cell(table_id, i, j, [100, 21, 199])

    if (app_data == 40 or app_data == 83) and hospital[i + 1][j] != 2 and hospital[i + 1][j] != 3:
        # SUD
        dpg.highlight_table_cell(table_id, i, j, [173, 216, 230])
        i = i + 1
        dpg.highlight_table_cell(table_id, i, j, [100, 21, 199])

    if hospital[i][j] == 4:
        with dpg.window(label="Congrats!"):
            dpg.add_text("You escaped!")


def move_prisoner1():
    dpg.highlight_table_cell(table_id, 10, 11, [173, 216, 230])

    for i in range(len(x1)):
        dpg.highlight_table_cell(table_id, x1[i], y1[i], [200, 0, 11])
        time.sleep(1.2)
        dpg.highlight_table_cell(table_id, x1[i], y1[i], [173, 216, 230])


def move_prisoner2():
    dpg.highlight_table_cell(table_id, 10, 13, [173, 216, 230])

    for i in range(len(x2)):
        dpg.highlight_table_cell(table_id, x2[i], y2[i], [250, 0, 11])
        time.sleep(0.6)
        dpg.highlight_table_cell(table_id, x2[i], y2[i], [173, 216, 230])


move_thread1 = threading.Thread(name="move", target=move_prisoner1, args=(), daemon=True)
move_thread2 = threading.Thread(name="move", target=move_prisoner2, args=(), daemon=True)
move_thread2.start()
move_thread1.start()

key_release_handler_parent = dpg.add_handler_registry()
dpg.add_key_release_handler(callback=move_player, parent=key_release_handler_parent)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
