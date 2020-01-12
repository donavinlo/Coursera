# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
def GCD(a,b):
    if b == 0:
        return a
    else:
        aprime = a % b
        return GCD(b, aprime)
def lcm(a,b):
    return int((a*b)/GCD(a,b))

if __name__ == '__main__':
    # input = sys.stdin.read();
    inp = input()
    a, b = map(int, inp.split())
    print(lcm(a, b))

