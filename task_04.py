import numpy as np

def print_evenly_spaced_array(start: int, stop: int, num: int) -> None:
    print(np.linspace(start, stop, num))

start_num = int(input("Enter start num: "))
end_num = int(input("Enter end num: "))
count = int(input("Enter count of numbers: "))

print_evenly_spaced_array(start_num, end_num, count)