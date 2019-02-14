from Tree.SegmentTree import SegmentTree
from Tree.BinaryTree import BinaryTree

st = SegmentTree([1,3,2,-2,4,5], 'min')
print(st)


b = BinaryTree([1,2,3,4,5])
print(b)
bt = b.binary_tree

print("Inorder Tree Traversal")
b.inorderTraversal(bt)
print("\nPreorder Tree Traversal")
b.preorderTraversal(bt)
print("\nPostorder Tree Traversal")
b.postorderTraversal(bt)
height = b.getHeight(bt)
print(height)


b.levelorderTraversal(bt)