# # Uses python3
import numpy as np

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
