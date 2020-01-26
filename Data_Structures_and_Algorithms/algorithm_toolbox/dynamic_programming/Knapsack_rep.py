# Uses python3
import sys

#You are given a set of bars of gold and your goal is to take as much gold as possible into
#your bag. There is just one copy of each bar and for each bar you can either take it or not
#(hence you cannot take a fraction of a bar).

def optimal_weight(capacity, weights, i, T = {}):
   if (capacity, i) not in T:
       if i == 0:
           T[capacity, i] = 0
       else:
           T[capacity, i] = optimal_weight(capacity, weights,i-1)
           if capacity >= weights[i-1]:
               T[capacity, i] = max(T[capacity, i],
                                    optimal_weight(capacity - weights[i-1], weights, i-1) + weights[i-1])
   return T[capacity,i]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n, {}))
