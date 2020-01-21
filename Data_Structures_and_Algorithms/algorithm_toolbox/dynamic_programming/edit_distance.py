# Uses python3
def edit_distance(s, t):
    i = len(s)
    j = len(t)
    if i == 0:
        return j
    if j == 0:
        return i



if __name__ == "__main__":
    print(edit_distance(input(), input()))
