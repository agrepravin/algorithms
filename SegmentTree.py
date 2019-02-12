# 1st: Linear approach will take O(j-i+1) time to compute min/max/sum for index (i, j) i.e. O(n) in General,
# Update takes only O(1) here
# 2nd: Building n x n matrix which will take O(n2) to build and O(1) to query after build but then updates are expensive, i.e. O(n2) if whole nxn matrix needs to be updated
# we can use this approach if updates are not required. But I do have issue when it comes to space complexity i.e. O(n2)
# 3rd: Storing frequency values then query would be f[r] - f[l-1]
# 4rd: Segment trees will take here O(log n) for query and update as well. Building a tree takes O(n) time

### Maximum array size required to build a tree of n i.e. (2 * (2 ** log n base 2 )) - 1 ==> (4 * n) + 1

from Tree import Tree

class SegmentTree(Tree):
    def __init__(self, arr, type='sum'):
        # Types can min/max/sum default is sum
        self.type = type
        self.length = 2 * len(arr) + 1
        self.temp = [-1] * self.length
        super().__init__(arr)

    def buildTree(self, arr):
        start = 0
        index = 0
        end = len(self.arr) - 1
        self.__buildTree(arr, start, end, index)

    def __buildTree(self, arr, start, end, index):
        """Build Segment tree"""
        if start == end:
            self.temp[index] = arr[start]
            return
        elif start > end:
            return

        mid = (start+end)//2
        self.__buildTree(arr, start, mid, 2 * index + 1)
        self.__buildTree(arr, mid + 1, end, 2 * index + 2)
        if self.type == 'sum':
            self.temp[index] = self.temp[2 * index + 1] + self.temp[2 * index + 2]
        elif self.type == 'min':
            self.temp[index] = min(self.temp[2 * index + 1], self.temp[2 * index + 2])
        elif self.type == 'max':
            self.temp[index] = max(self.temp[2 * index + 1], self.temp[2 * index + 2])

        return