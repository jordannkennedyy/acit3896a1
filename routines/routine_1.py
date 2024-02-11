import random
import time
import myfuncs
import matplotlib.pyplot as plt
import numpy as np
import csv


def fut(case):
    fut2(case, 0, len(case) - 1)
    return case


def fut2(case, s, t):
    if t < s:
        return
    if case[s] > case[t]:
        case[s], case[t] = case[t], case[s]
    if t > s + 1:
        q = (t - s + 1) // 3
        fut2(case, s, t - q)
        fut2(case, s + q, t)
        fut2(case, s, t - q)


def casemaker(size):
    return [random.randint(0, 1e9) for _ in range(size)]



# --------------------------------------- TIMER ----------------------------------------------- #
# pass casemaker to fut

def final_collection(case, increment):
    collect_time_list_of_dictionaries = []
    timer = case
    i = increment
    while i < timer:
        start_time = time.perf_counter_ns()
        get_number = fut(casemaker(i))
        end_time = time.perf_counter_ns()
        final_time = end_time - start_time
        convert_to_seconds = myfuncs.nano_to_sec(final_time)
        collect_time_list_of_dictionaries.append({'N': i, 'Time': convert_to_seconds})
        i += increment
    return collect_time_list_of_dictionaries


# ----------------------------------------------- COLLECT DATA ------------------------------------------------ #

# 10**6 = > 1 hr 30 min (too long)
# 10 **4 = > 40 min

# data = final_collection(10**3.7, 100)

# # write results to text file
# field_names = ["N", "Time"]
# with open('./data/routine1.csv', 'a') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(data)


# ----------------------------------------------- GRAPH ----------------------------------------------------------#

y_values = []
x_values =[]
with open('./data/routine1.csv', 'r', newline='') as csvfile:
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
        my_time = 0.01 * pow(2, float(num)/100)
        # my_time = 0.03 * np.log(2, float(num))
        y_values.append(my_time)
    return y_values

new_y = test_plot(x_values)

fig, axs = plt.subplots()
# plt.plot(x_values, y_values, linestyle='-', marker='o', color='red', label='First Test')
plt.plot(x_values, new_y, linestyle='-', marker='o', color='blue', label='My Calculation')
plt.xlabel("N (Int)")
plt.ylabel("Time (Sec)")
plt.title(f"Routine 1 (Total Time: {get_time(y_values)})")
plt.legend()
plt.show()
        


