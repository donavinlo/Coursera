# Uses python3
import sys

# Find the majority of the list using divide and conquer (MergeSort used in this example)
def get_majority_element(a, left, right):
    #Base Cases
    if left == right:
        return a[left]
    if left + 1 == right:
        return a[left]
    m = (left + right - 1) // 2
    
    #Run recursively to get left majority and right majority
    leftm = get_majority_element(a, left, m + 1)
    rightm = get_majority_element(a, m + 1, right)
    
    #Get count of left majority in full string
    left_count = 0
    for i in range(left, right):
        if a[i] == leftm:
            left_count += 1
    if left_count > (right - left) // 2:
        return leftm
    
    Get  count of right majority in full string
    right_count = 0
    for i in range(left, right):
        if a[i] == rightm:
            right_count += 1
    if right_count > (right - left) // 2:
        return rightm
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
