# Merge sort follows divide-conquer method to achieve sorting
# As it divides array into half until one item is left these is done in O(log n) time complexity
# While merging it linear compare items and merge in order which is achieved in O(n) time complexity
# Total time complexity for MergeSort is O(n log n) in all three cases

from Sorting.Sorting import Sorting


class MergeSort(Sorting):

    def sort(self):
        if len(self.arr) > 1:
            mid = len(self.arr)//2
            left = self.arr[:mid]
            right = self.arr[mid:]
            L = MergeSort(left)
            L.sort()
            R = MergeSort(right)
            R.sort()

            i=j=k=0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.arr[k] = left[i]
                    i += 1
                else:
                    self.arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                self.arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                self.arr[k] = right[j]
                j += 1
                k += 1
