# Uses python3
def edit_distance(s, t, vals = None):
    if vals is None:
        vals = {}
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)
    if (len(s), len(t)) in vals:
        return vals[len(s), len(t)] 
    if s[-1] != t[-1]:
        penalty = 1
    else:
        penalty = 0
    diag = edit_distance(s[:-1], t[:-1], vals) + penalty
    vert = edit_distance(s[:-1], t, vals) + 1
    horz = edit_distance(s, t[:-1], vals) + 1
    ans = min(diag, vert, horz)
    vals[len(s), len(t)] = ans
    return ans

if __name__ == "__main__":
    print(edit_distance(input(), input()))
