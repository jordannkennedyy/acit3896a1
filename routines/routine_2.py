import random
import time
from myfuncs import nano_to_sec
import matplotlib.pyplot as plt
import numpy as np
import csv


def fut(case):
    h, n = case
    l = 0
    r = len(h)
    while r > l:
        time.sleep(0.0001)
        m = (r + l) // 2
        if h[m] == n:
            return m
        elif h[m] > n:
            r = m
        else:
            l = m


def casemaker(size):
    start = random.randint(1, 10 * size) + size
    step = random.randint(1, 10)
    oof = range(start, start + (size + 2) * step, step)
    return [oof, oof[random.randint(1, len(oof)) - 1]]



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
        convert_to_seconds = nano_to_sec(final_time)
        collect_time_list_of_dictionaries.append({'N': i, 'Time': convert_to_seconds})
        i += increment
    return collect_time_list_of_dictionaries


# --------------------------------------- COLLECT DATA ------------------------------------------------ #
# write results to text file
# 10**7 = 5 min
# 10**8 or **9
# longer ----> 10**8 or 9

# data = final_collection(10**7.5, 100)

# field_names = ["N", "Time"]
# with open('./data/routine2.csv', 'a') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(data)



# seems to be constant

# --------------------------------------- PLOT ------------------------------------------------ #
    
    
y_values = []
x_values =[]
with open('./data/routine2.csv', 'r', newline='') as csvfile:
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
    min = sec / 60
    return min


fig, axs = plt.subplots()
plt.plot(x_values[1:30], y_values[1:30], linestyle='-', marker='o', color='red', label='First Test')
plt.xlabel("N (Int)")
plt.ylabel("Time (Sec)")
plt.title("Routine 2")
plt.legend()
plt.show()
