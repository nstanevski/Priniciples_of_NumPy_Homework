import numpy as np


def null_array_of_length(num: int) -> None:
    null_array = np.zeros(num)
    print(null_array)


# Read input from the user
n = int(input("Enter the value of n: "))


# Call the function to print the null array
null_array_of_length(n)
