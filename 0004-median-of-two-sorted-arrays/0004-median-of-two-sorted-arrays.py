import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        arr = np.concatenate((nums1, nums2))
        arr.sort()


        return statistics.median(arr)



