# # Uses python3
import numpy as np
# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib(n - 1) + calc_fib(n - 2)

def FibList(n):
    arr = np.zeros(n+1)
    arr[0] = 0
    if n >= 1:
        arr[1] = 1
    for i in range(2, n + 1 ):
        arr[i] = (arr[i-1] + arr[i-2])
    return int(arr[n])

n = int(input())
print(FibList(n))
