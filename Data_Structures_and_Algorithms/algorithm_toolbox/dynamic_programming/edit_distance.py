# Uses python3
## return the edit distance using dynamic programming
def edit_distance(s, t, vals = None):
    if vals is None:
        vals = {}
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)
    if (len(s), len(t)) in vals:
        return vals[len(s), len(t)] #same operation for mathc/mismatch but match you add 1
    if s[-1] != t[-1]:
        match = edit_distance(s[:-1], t[:-1], vals) + 1
    else:
        match= edit_distance(s[:-1], t[:-1], vals)
    deletion = edit_distance(s[:-1], t, vals) + 1
    insertion = edit_distance(s, t[:-1], vals) + 1
    ans = min(match, deletion, insertion)
    vals[len(s), len(t)] = ans
    return ans

if __name__ == "__main__":
    print(edit_distance(input(), input()))
