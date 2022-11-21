from operator import length_hint
import sys
import numpy as np
import random
import time
import threading
import dearpygui.dearpygui as dpg
from Patient import Patient

hospital = np.random.randint(3, size=(20, 25))

print(time.perf_counter())
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

with dpg.window(label="Mental hospital", tag="hospital", width=900, height=700):
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
                        x1[i] = 0
                        y1[i] = 0

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
name = input("Enter name")
age = input("Enter age")
weight = int(input("Enter weight"))
height = int(input("Enter height"))/100
illness = input("Enter illness")

patient_you = Patient(name, age, weight/height*height, illness, 0)
for i in range(len(x)):
    print(x[i], end=' ')

time1 = time.perf_counter()
print("time1", time1)
i = 10
j = 12
last_x = 10
last_y = 12

illnesses = ["Schizofrenie", "Parkinson", "Tulburare bipolara", "Alzheimer"]

counter = 0


def guard(patient):
    with dpg.window(label="Gardianul Greedy", width=900, height=700):
        friends = random.randint(5, 10)
        dpg.add_text(
            "La iesirea din spital ai dat de Gardianul Greedy si de " + patient.get_name() + " care a evadat inaintea ta si a a adus cu el inca " +
            str(friends) + "prieteni", tag="text1")
        time.sleep(0.5)
        dpg.add_separator()
        dpg.add_text("Gardianul Greedy va lasa sa evadeze doar " + str(friends - 2) +
                     " prizonieri, evaluandu-va in parte si va alcatui o lista.", tag="text2")
        time.sleep(3)
        dpg.delete_item("text1")
        dpg.delete_item("text2")
        dpg.add_loading_indicator()
        dpg.add_text("Gardianul se gandeste...")
        if greedy(friends, patient) is True:
            escaped()
        else:
            returned()


def greedy(friends, patient):
    friends_arr = [patient_you, patient]
    for i in range(friends):
        friends_arr.append(
            Patient("friend" + str(i), random.randint(20, 50), random.randint(17, 30),
                    illnesses[random.randrange(0, 4)],
                    patient.get_time()))

    print("mivi3jnvitnvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    for i in range(friends):
        print(friends_arr[i].get_illness())

    print("mivi3jnvitnvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")

    mark = {}

    for i in range(len(friends_arr) - 1):
        for j in range(i, len(friends_arr)):
            if 18.5 < friends_arr[j].get_bmi() < friends_arr[i].get_bmi():
                aux = friends_arr[i]
                friends_arr[i] = friends_arr[j]
                friends_arr[j] = aux

    for i in range(len(friends_arr)):
        mark[friends_arr[i]] = i * 3 - illnesses.index(friends_arr[i].get_illness())
        if friends_arr[i].get_age() > 40:
            mark[friends_arr[i]] = mark[friends_arr[i]] + 2

    friends_sorted = sorted(mark.items(), key=lambda x: x[1])
    for i in range(len(friends_sorted)):
        print(friends_sorted[i])

    keys = list(mark.keys())
    for i in range(friends-2):
        print(keys[i].get_name())
        if keys[i].get_name() == patient_you.get_name():
            return True
    return False


def escaped():
    with dpg.window(label="Felicitari!", width=900, height=700):
        dpg.add_text("Ai evadat din spital!")

def returned():
    with dpg.window(label="Esti un fraier!", width=900, height=700):
        dpg.add_text("Meriti sa te intorci la soarta ta mizerabila:))...Better luck next time")


def schizo():
    global counter
    if counter % 5 == 0 and random.randrange(0, 2) == 1:

        with dpg.window(label="Warning!", modal=True, show=True, tag="modal_id", no_title_bar=True, height=300,
                        width=300):
            width, height, channels, data = dpg.load_image("schizo.png")
            with dpg.texture_registry(show=False, tag="registry"):
                dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

            dpg.add_text("Ai un episod schizofrenic!")
            dpg.add_image("texture_tag", tag="image")
            time.sleep(3)
            dpg.delete_item("modal_id")
            dpg.delete_item("image")
            dpg.delete_item("texture_tag")
            dpg.delete_item("registry")


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


def funct():
    time2 = time.perf_counter()
    print("time2", time2)
    patient1 = Patient("Vasile", 29, 30, illnesses[random.randrange(0, 4)], 1.2 * len(np.trim_zeros(x1)))
    print("patient1", patient1.get_time())

    patient2 = Patient("Constantin", 40, 35, illnesses[random.randrange(0, 4)], 0.6 * len(x2))
    print("patient2", patient2.get_time())

    print(time2 - time1)

    if time2 - time1 < patient1.get_time() and time2 - time1 < patient2.get_time():
        print("da")
        escaped()
    elif patient1.get_time() < time2 - time1 < patient2.get_time():
        print("bcernuvn")
        guard(patient2)
    elif patient2.get_time() < time2 - time1 < patient1.get_time():
        guard(patient1)
    else:
        returned()


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
        time.sleep(2)
        dpg.delete_item("hospital")
        funct()


steps1 = 0
steps2 = 0

print(x1)


def move_prisoner1():
    dpg.highlight_table_cell(table_id, 10, 11, [173, 216, 230])

    global steps1
    for i in range(len(x1)):
        steps1 = steps1 + 1
        if x1[i] == 0 and y1[i] == 0:
            break
        else:
            dpg.highlight_table_cell(table_id, x1[i], y1[i], [200, 0, 11])
            time.sleep(1.2)
            dpg.highlight_table_cell(table_id, x1[i], y1[i], [173, 216, 230])


def move_prisoner2():
    dpg.highlight_table_cell(table_id, 10, 13, [173, 216, 230])

    global steps2
    for i in range(len(x2)):
        steps2 = steps2 + 1
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
