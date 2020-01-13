# Uses python3
import sys

def get_optimal_value(capacity, weights, indvalues):
    totvalue = 0
    A = []
    for i in range(len(weights)):
        ind_wt = indvalues[i] / weights[i]
        A.append([weights[i],  indvalues[i], ind_wt])
        A.sort(reverse=True, key = lambda x: x[2])
    if capacity == 0:
        return 0
    for i in A:
        curweight = int(i[0])
        curval = int(i[1])

        if capacity - curweight >= 0:
            capacity -=curweight
            totvalue += curval
        else:
            a = capacity / curweight
            totvalue += curval * a
            capacity = int(capacity - (curweight * a))
            break
    return totvalue

if __name__ == "__main__":
    data = [int(x.strip()) for line in sys.stdin.readlines() for x in line.split()]
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2] # every two values from index two until one less than  2 times the number of values
    weights = data[3:(2 * n + 2):2] #plus two. (2 fo n and capacity and then 2 *n because interchanging value and weight
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

