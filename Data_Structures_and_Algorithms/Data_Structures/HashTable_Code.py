#python 3

class HashTable:
    def __init__(self, size = 0):
        self.size = size
        self.hash_table =[[] for _ in range(self.size)] # size for array of linked lists (m)

    def hash_function(self, key):
        '''function used to create the hash key'''
        return key % self.size


    def insert(self, key, value):
        '''insert function of a hash table'''
        hash_key = self.hash_function(key)
        key_exists = False
        link_list = self.hash_table[hash_key]
        for i, kv in enumerate(link_list):
            k,v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            print('x')
            link_list[i] = ((key,value))
        else:
            link_list.append((key,value))

    def search(self, key):
        hash_key = self.hash_function(key)
        link_list = self.hash_table[hash_key]
        for i, kv in enumerate(link_list):
            k,v = kv
            if key == k:
                return v
        return 'This Key Doesn\'t exist.'

    def delete(self, key):
        hash_key = self.hash_function(key)
        key_exists = False
        link_list = self.hash_table[hash_key]
        for i, kv in enumerate(link_list):
            k, v = kv
            if key == k:
                key_exists = True
                del link_list[i]
                break
        if key_exists:
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))

    def print_HashTable(self):
        print(self.hash_table)

if __name__ == '__main__':
    # hash = HashTable(size=10)
    # hash.insert(10, 'Donavin')
    # hash.insert(23, 'Chocolate')
    # hash.print_HashTable()
    # hash.search(23)
    # hash.delete((23))
    # hash.print_HashTable()
    for i in range(5,-1, -1):
        print(i)