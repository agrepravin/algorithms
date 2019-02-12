from Tree import Tree


class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree(Tree):
    def __init__(self, arr):
        self.binary_tree = None
        super().__init__(arr)

    def buildTree(self, arr):
        n = len(self.arr) - 1
        root = None
        self.binary_tree = self.__buildTree(arr, root, 0, n)

    def __buildTree(self, arr, root, i, n):

        if i < n:
            temp = Node(arr[i])
            root = temp

            root.left = self.__buildTree(arr, root.left, 2 * i + 1, n)
            root.right = self.__buildTree(arr, root.right, 2 * i + 2, n)

        return root