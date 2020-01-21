# Uses python3
import sys
# given m find how to make get change with the minimum number of coins 
def get_change(m):
    coins = [1,3,4]
    if T[m] != 0:
        return T[m]
    if m < 0:
        return 0
    if m == 0:
        T[m] = 0
    if m not in T:
        T[m] = float('inf')
        for i in range(len(coins)):
            if m >= coins[i]:
                T[m] = min(T[m], get_change(m - coins[i]) + 1)
    return T[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    T = [0] * (m+1)
    print(get_change(m))
