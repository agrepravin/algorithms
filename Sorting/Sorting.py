from abc import ABC, abstractmethod

class Sorting(ABC):
    def __init__(self, arr):
        self.arr = arr
        super().__init__()


    @abstractmethod
    def sort(self):
        pass


    def printArray(arr):
        """ If array is sorted will print sorted array or else as it is"""
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()


    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.arr)