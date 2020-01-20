# Uses python3
import sys

def optimal_sequence(n):
    arr = [0] * (n + 1)
    sequence = []
    if n == 1:
        sequence.append(1)
        return sequence
    else:
        for i in range(2, n + 1):
            if (i < 4):
                arr[i] = 1
            elif (i % 3 == 0 and i % 2 != 0):
                if (arr[i // 3] < arr[i - 1]):
                    arr[i] = arr[i // 3] + 1
                else:
                    arr[i] = arr[i - 1] + 1
            elif (i % 2 == 0 and i % 3 != 0):
                if (arr[i // 2] < arr[i - 1]):
                    arr[i] = arr[i // 2] + 1
                else:
                    arr[i] = arr[i - 1] + 1
            elif (i % 3 != 0 and i % 2 != 0):
                arr[i] = arr[i - 1] + 1
            else:
                if (arr[i // 2] < arr[i // 3]):
                    arr[i] = arr[i // 2] + 1
                else:
                    arr[i] = arr[i // 3] + 1

    while n > 0:
        sequence.append(n)
        if (n % 2 == 0 and n % 3 != 0):
            if (arr[n - 1] < arr[n // 2]):
                n = n - 1
            else:
                n = n // 2
        elif (n % 2 == 0 and n % 3 == 0):
            n = n // 3
        elif (n % 2 != 0 and n % 3 != 0):
            n = n - 1
        elif (n % 2 != 0 and n % 3 == 0):
            if (arr[n - 1] < arr[n // 3]):
                n = n - 1
            else:
                n = n // 3
                
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
