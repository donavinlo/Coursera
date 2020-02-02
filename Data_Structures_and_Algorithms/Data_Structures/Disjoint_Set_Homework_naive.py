smallest = []
def MakeSet(i):
    smallest.append(i)

def Find(i):
    return smallest[i]

def Union(i,j):
    ''''Naive Implementation of disjoints sets'''
    i_id = Find(i)
    j_id = Find(j)
    if i_id == j_id:
        return
    m = min(i_id,j_id)
    for k in range(len(smallest)):
        if smallest[k] in {i_id, j_id}:
            smallest[k] = m
if __name__ == '__main__':
    for i in range(13):
        MakeSet(i)
    Union(2, 10)
    Union(7, 5)
    Union(6, 1)
    Union(3, 4)
    Union(5, 11)
    Union(7, 8)
    Union(7, 3)
    Union(12, 2)
    Union(9, 6)
    print(Find(6))
    print(Find(3))
    print(Find(11))
    print(Find(9))

