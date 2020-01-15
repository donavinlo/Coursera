# Uses python3
import sys
import math
import numpy as np

def binary_search_recursive(a, x, h , l=0): # x = 4
    a.sort()
    if l> h:
        return -1
    mid =  (h + l) // 2
    if x == a[mid]:
         return mid
    elif x < a[mid]:
        return binary_search_recursive(a,x, h = mid - 1, l=l)
    else:
        return binary_search_recursive(a,x, l=mid+1, h=h)

def binary_loop(a,x):
    l= 0
    h = len(a) - 1

    while l <= h:
        mid = (l+h) // 2
        if a[mid] < x:
            l = mid + 1
        else:
            h = mid - 1
    if l == len(a) or a[l] != x:
        return -1
    else:
        return l

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_loop(a,x), end = ' ')

