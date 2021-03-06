# python3
# Learning how to implement Object-Oriented programming while learning effecient algorithms 
class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        '''' read data from the main program'''
        n = int(input())
        self._data = [-1]
        self._data += [int(s) for s in input().split()]
        assert n == len(self._data) - 1

    def WriteResponse(self):
        '''write out output as requested format'''
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def SiftDown(self, i):
        '''sift down technique to sort the algorithm in the correct order'''
        min_i = i
        left = 2 * i
        right = 2 * i + 1

        if left <= len(self._data) - 1 and self._data[left] < self._data[min_i]:
            min_i = left
        if right <= len(self._data) - 1 and self._data[right] < self._data[min_i]:
            min_i = right
        if i != min_i:
            self._swaps.append((i - 1, min_i - 1))
            self._data[i], self._data[min_i] = self._data[min_i], self._data[i]
            self.SiftDown(min_i)

    def GenerateSwaps(self):
        '''initiates the swapping of elements in the array'''
        for i in range((len(self._data) - 1) // 2, 0, -1):
            self.SiftDown(i)

    def Solve(self):
        ''''Main Program we run'''
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
