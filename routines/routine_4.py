import random
import time
from myfuncs import nano_to_sec
import matplotlib.pyplot as plt
import numpy as np
import csv



def fut(case):
    result = 0
    trials = ["1"]
    while True:
        result += 1
        if "".join(trials) == case:
            return result
        i = len(trials) - 1
        while trials[i] == "1":
            trials[i] = "0"
            i -= 1
        if i == -1:
            trials = ["1"] + trials
        else:
            trials[i] = "1"
        if result > 1e24:
            return "WAT"


def casemaker(size):
    return "1" + "".join(random.choices("10", k=size))



# --------------------------------------- COLLECT DATA ----------------------------------------------- #
# pass casemaker to fut
# 1000000 = ?
# 25 = 6

def final_collection(case, increment):
    collect_time_list_of_dictionaries = []
    timer = case
    i = increment
    while i < timer:
        start_time = time.perf_counter_ns()
        get_number = fut(casemaker(i))
        end_time = time.perf_counter_ns()
        final_time = end_time - start_time
        convert_to_seconds = nano_to_sec(final_time)
        collect_time_list_of_dictionaries.append({'N': i, 'Time': convert_to_seconds})
        i += increment
    return collect_time_list_of_dictionaries


# --------------------------------------- COLLECT DATA ------------------------------------------------ #
# 100
# 50 > 3hrs
# data = final_collection(30, 1)


# field_names = ["N", "Time"]
# with open('./data/routine4.csv', 'a') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(data)


# --------------------------------------- PLOT ------------------------------------------------ #

y_values = []
x_values =[]
with open('./data/routine4.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for key in row:
            if key == 'N':
                x_values.append(row[key])
            else:
                y_values.append(row[key])

def get_time(list):
    mytime = [float(num) for num in list]
    sec = round(sum(mytime), 2)
    min = round(sec / 60, 2)
    return min

def test_plot(n_values):
    y_values = []
    for num in n_values:
        my_time = 1 * pow(2, float(num)/1)
        y_values.append(my_time)
    return y_values

new_y = test_plot(x_values)
new_y.sort()

fig, axs = plt.subplots()
# plt.plot(x_values, y_values, linestyle='-', marker='o', color='red', label='First Test')
plt.plot(x_values, new_y, linestyle='-', marker='o', color='blue', label='My Calculation')
plt.xlabel("N (Int)")
plt.ylabel("Time (Sec)")
plt.title(f"Routine 4 (Total Time: {get_time(y_values)} min)")
plt.legend()
plt.show()

