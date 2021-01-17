import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2) # tack on num2 to nums1
        sort = sorted(nums1) # sort nums1
        
        # Check if the merged array has an even or odd number of elements
        if len(sort) % 2 != 0:
            
            # if number of elements is odd, then the median is at index of 1
            # less than length divided by 2
            return float(sort[(len(sort) - 1) // 2])
        else:
            
            # if even number of elements, then the median is half of the sum of 
            # the num at an index of half the length and one less than half the length
            first = len(sort) // 2
            second = first - 1
            return (sort[first] + sort[second]) / 2