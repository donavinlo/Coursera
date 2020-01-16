# Uses python3
import sys

def get_majority_element(a, left, right):
    n = len(a)
    a.sort()
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    for i in range(right):
        if


    return -1



# def MergeSort(a, left, right):
#     m = n // 2
#     if len(a) == 1:
#         return a
#     b = MergeSort(a[1:m +1])
#     c = MergeSort(a[m+1:])
#     a_prime = merge(b,c)
#     return a_prime
#
# def Merge(b,c):
#     d = []
#     for i in range(len(b)+len(q)):
#         if




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if mergeSort(a) != -1:
        print(1)
    else:
        print(0)
