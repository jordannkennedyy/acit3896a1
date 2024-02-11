import random
import matplotlib.pyplot as plt
import numpy as np
import time
from myfuncs import nano_to_sec
import csv


def fut(case):
    i = 1
    while i < len(case):
        if i == 0 or case[i] >= case[i - 1]:
            i += 2
        else:
            case[i], case[i - 1] = case[i - 1], case[i]
        i -= 1
    return case


def casemaker(size):
    return [random.randint(0, 1e9) for _ in range(size)]



# --------------------------------------- TIMER ----------------------------------------------- #
# pass casemaker to fut
# 10000 = 5sec
# 100000 = ?


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
# 40000 = 24 min
# 10 ** 5 = 31 min
# data = final_collection(25000, 100)

# field_names = ["N", "Time"]
# with open('./data/routine5.csv', 'a') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(data)



# ----------------------------------------- PLOT ------------------------------------------------ #
y_values = []
x_values =[]
with open('./data/routine5.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for key in row:
            if key == 'N':
                x_values.append(row[key])
            else:
                y_values.append(row[key])

def get_sample_of_10(list):
    sample = []
    index = 0
    while index < len(list):
        sample.append(list[index])
        index = index + 25
    return sample

# y_values_sample = get_sample_of_10(y_values)
# x_values_sample = get_sample_of_10(x_values)
# print(y_values_sample)
# print(x_values_sample)

def get_time(list):
    mytime = [float(num) for num in list]
    sec = round(sum(mytime), 2)
    min = round(sec / 60, 2)
    return min

def test_plot(n_values):
    count = 0
    y_values = []
    for num in n_values:
        my_time = 100/0.03 * float(num)
        y_values.append(my_time)
    return y_values

new_y = test_plot(x_values)
new_y.sort()

y_values.sort()
fig, axs = plt.subplots()
# plt.plot(x_values[30:60], y_values[30:60], linestyle='-', marker='o', color='red', label='First Test')
plt.plot(x_values[30:60], new_y[30:60], linestyle='-', marker='o', color='blue', label='My Calculation')
plt.xlabel("N (Int)")
plt.ylabel("Time (Sec)")
plt.title(f"Routine 5 (Total Time: {get_time(y_values)} min)")
plt.legend()
plt.show()