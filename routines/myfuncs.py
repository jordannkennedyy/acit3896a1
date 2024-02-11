import math
import time

def nano_to_sec(time_1):
    return round(time_1 / 10**9, 2)

def my_awesome_timer(item_to_time):
    start_time = time.perf_counter_ns()
    results = item_to_time
    end_time = time.perf_counter_ns()
    final_time = end_time - start_time
    convert_to_seconds = nano_to_sec(final_time)
    return convert_to_seconds


def my_awesome_data_collector(item_to_collect):
    results = item_to_collect
    return results