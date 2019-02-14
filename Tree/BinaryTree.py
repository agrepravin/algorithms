from Tree.Tree import Tree


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
        n = len(self.arr)
        root = None
        self.binary_tree = self.__buildTree(arr, root, 0, n)

    def __buildTree(self, arr, root, i, n):

        if i < n:
            temp = Node(arr[i])
            root = temp

            root.left = self.__buildTree(arr, root.left, 2 * i + 1, n)
            root.right = self.__buildTree(arr, root.right, 2 * i + 2, n)

        return root

    def inorderTraversal(self, binary_tree):
        if binary_tree:
            self.inorderTraversal(binary_tree.left)
            print(binary_tree.value, end="  ")
            self.inorderTraversal(binary_tree.right)


    def preorderTraversal(self, binary_tree):
        if binary_tree:
            print(binary_tree.value, end="  ")
            self.preorderTraversal(binary_tree.left)
            self.preorderTraversal(binary_tree.right)

    def postorderTraversal(self, binary_tree):
        if binary_tree:
            self.postorderTraversal(binary_tree.left)
            self.postorderTraversal(binary_tree.right)
            print(binary_tree.value, end="  ")


    def levelorderTraversal(self, binary_tree):
        level = self.getHeight(binary_tree)
        for i in range(1, level+1):
            BinaryTree.__printGivenLevel(binary_tree, i)
            print()


    @staticmethod
    def __printGivenLevel(binary_tree, level):
        if binary_tree == None:
            return
        if level == 1:
            print(binary_tree.value, end=" ")
        elif level > 1:
            BinaryTree.__printGivenLevel(binary_tree.left, level - 1)
            BinaryTree.__printGivenLevel(binary_tree.right, level - 1)


    def getHeight(self, binary_tree):

        if binary_tree == None:
            return 0
        else:
            h = max(self.getHeight(binary_tree.left) + 1, self.getHeight(binary_tree.right) + 1)
            return h

