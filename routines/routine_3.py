import random
import time
from myfuncs import nano_to_sec
import matplotlib.pyplot as plt
import numpy as np
import csv



def fut(case):
    h, n = case
    mp8 = 2**31 - 1
    i = 0
    while h[i] != n:
        i = (i + mp8) % len(h)
        if i == 0:
            return None
    return i


def casemaker(size):
    oof = [random.randint(0, int(1e6)) for _ in range(size)]
    for i in range(1, len(oof)):
        oof[i] += oof[i - 1]
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
# 1000000 = ?
# 10**8 = probably good
# longer --> 10**7 or 8

# data = final_collection(10**6.5, 1000)

# field_names = ["N", "Time"]
# with open('./data/routine3.csv', 'a') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(data)



# --------------------------------------- PLOT ------------------------------------------------ #
y_values = []
x_values =[]
with open('./data/routine3.csv', 'r', newline='') as csvfile:
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
        index = index + 300
    return sample

# y_values_sample = get_sample_of_10(y_values)
# x_values_sample = get_sample_of_10(x_values)
# print(x_values_sample)
# print(y_values_sample)


def get_time(list):
    mytime = [float(num) for num in list]
    sec = round(sum(mytime), 2)
    min = sec / 60
    return min


fig, axs = plt.subplots()
plt.plot(x_values, y_values, linestyle='-', marker='o', color='red', label='First Test')
plt.xlabel("N (Int)")
plt.ylabel("Time (Sec)")
plt.title(f"Routine 3 (Total Time: {get_time(y_values)}) min")
plt.legend()
plt.show()