import numpy as np
import random
import time
import threading

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

hospital = np.random.randint(3, size=(20, 25))
#
cnt = 0

hospital[0][0] = 3
hospital[19][0] = 3
hospital[0][24] = 3
hospital[19][24] = 3

hospital[10][11] = 0
hospital[10][13] = 0

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
dpg.configure_viewport(0, x_pos=0, y_pos=0, width=1000, height=790)

#
# hospital = [[1, 0, 0, 1],
#             [1, 0, 1, 0],
#             [0, 0, 1, 0],
#             [0, 1, 1, 1]]

m = 20
n = 25

path = np.zeros((m + 1, n + 1), dtype=int)

coord1 = [1, 0, -1, 0]
coord2 = [0, 1, 0, -1]

x = []
y = []


def show():
    for i in range(m):
        for j in range(n):
            print(path[i][j], end=' ')
        print('\n')
    print('\n')

    for i in range(len(x)):
        print(x[i] , "     ", y[i])
    print('\n')

    # def move():
    #
    #     dpg.highlight_table_cell(table_id, 2, 3, [200, 0, 11])
    #     dpg.unhighlight_table_cell(table_id, 2, 3)

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
                            elif hospital[i][j] == 4:
                                dpg.highlight_table_cell(table_id, i, j, [85, 187, 51])
                                dpg.add_text("EXIT")
                            elif hospital[i][j] == 3 or hospital[i][j] == 2:
                                dpg.highlight_table_cell(table_id, i, j, [66, 73, 82])

    dpg.highlight_table_cell(table_id, 10, 12, [100, 20, 400])
    dpg.highlight_table_cell(table_id, 10, 11, [200, 0, 11])
    dpg.highlight_table_cell(table_id, 10, 13, [298, 0, 29])

    def move_prisoner():
        dpg.highlight_table_cell(table_id, 10, 11, [0, 0, 0])
        for i in range(len(x)):
            dpg.highlight_table_cell(table_id, x[i], y[i], [200, 0, 11])
            time.sleep(0.3)
            dpg.highlight_table_cell(table_id, x[i], y[i], [173, 216, 230])
            print('\n')
        print('\n')

    move_thread = threading.Thread(name="move", target=move_prisoner, args=(), daemon=True)
    move_thread.start()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def valid(ii, jj):
    if ii < 0 or ii > m - 1 or jj < 0 or jj > n - 1: return False
    if hospital[ii][jj] == 2 or hospital[ii][jj] == 3: return False
    if path[ii][jj] != 0: return False
    return True


def backtracking(i, j, pas):
    for k in range(4):
        ii = i + coord1[k]
        jj = j + coord2[k]

        x.append(ii)
        y.append(jj)

        if valid(ii, jj) is True:
            path[ii][jj] = pas + 1
            if hospital[ii][jj] == 4:
                show()
            else:
                backtracking(ii, jj, pas + 1)
            path[ii][jj] = 0

        x.pop(len(x) - 1)
        y.pop(len(y) - 1)


for i in range(m):
    for j in range(n):
        print(hospital[i][j], end=' ')
    print('\n')

print('\n')
path[10][11] = 1
hospital[10][11] = 0

for i in range(m):
    for j in range(n):
        print(path[i][j], end=' ')
    print('\n')
cnt = 0
backtracking(10, 11, 1)
