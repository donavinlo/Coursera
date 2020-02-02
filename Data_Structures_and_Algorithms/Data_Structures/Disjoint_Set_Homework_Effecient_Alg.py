parent = []
rank = []

def MakeSet(i):
    ''' Creates an array for that that represent the parent and rank of each node of the tree'''
    parent.append(i)
    rank.append(0)

def Find(i):
    '''returns the parent for a particular node'''
    if i != parent[i]:
        i = parent[i]
    return i
def Union(i,j):
    '''Finds the parent of each node and compares the rank. Whichever parent has the higher rank is considered the root
        for that subtree. If j_id (parent of j) has a higher rank or the ranks are both equal then j_id becomes the root
        of the subtree. Also, the rank is updated by 1.'''
    i_id = Find(i)
    j_id = Find(j)
    if i_id == j_id:
        return
    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
    else:
        parent[i_id] = j_id
        if rank[i_id] == rank[j_id]:
            rank[j_id] = rank[j_id] + 1

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

