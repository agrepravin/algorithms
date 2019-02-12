from abc import ABC, abstractmethod


class Tree(ABC):
    """Abstract class to build all types of Trees"""
    def __init__(self, arr):
        self.arr = arr
        self.buildTree(arr)
        super().__init__()


    @abstractmethod
    def buildTree(self, arr):
        pass


    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.arr)
