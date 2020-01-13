# Uses python3
import sys
import numpy as np
def get_change(m):
        total = 0
        count = 0
        while total < m:
            if (m - total) >= 10:
                total += 10
                count += 1
            if (m - total) >= 5 and (m -total) < 10:
                total += 5
                count += 1
            if (m - total) < 5 and (m - total) > 0:
                total +=1
                count += 1
        return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
