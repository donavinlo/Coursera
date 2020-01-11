# python3
import numpy as np

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def MaxPairwiseProductFast(numbers):
    numbers = sorted(numbers, reverse =True)
    max_product = numbers[0] * numbers[1]
    return max_product

def stress_test(n, m):
    ''' n represents the max length of the list while m represents the range of values of that can be put in n'''
    try:
        while True:
            length = np.random.randint(low=2, high= n)
            max_val = np.random.randint(low=3, high=m)
            arr = np.random.randint(low=2, high=max_val, size = length)
            print(arr)
            res1 = max_pairwise_product(arr)
            res2 = max_pairwise_product_fast(arr)
            print('Fast: {}, Naive: {}'.format(res2, res1))
            if res1 == res2:
                print('OK')
            else:
                print('Wrong Answer: {} , {}'.format(res1, res2))
            print('                                                     ')
    except:
        if n <= 2 or m <= 3:
            print('You must enter a value larger than 2 for n and 3 for m')
        else:
            print['Sorry we have encountered an issue']



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    result = MaxPairwiseProductFast(input_numbers)
    print(result)
    # print(max_pairwise_product(input_numbers))
    # print(max_pairwise_product_fast(input_numbers))
