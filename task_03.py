import  numpy as np

def print_identity_matrix(n: int) -> None:
    print(np.identity(n))

num_rows = int(input("Enter the value of n: "))

print_identity_matrix(num_rows)