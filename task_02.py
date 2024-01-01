import numpy as np

def print_consecutive_array(s: int, e: int) -> None:
    cons_arr = np.arange(s, e+1)
    print(cons_arr)

start_num = int(input("Enter start num: "))
end_num = int(input("Enter end num: "))
print_consecutive_array(start_num, end_num)
