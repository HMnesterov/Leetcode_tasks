class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        nums1.extend(nums2)
        nums1.sort()
        len_spis = len(nums1)
        if len_spis % 2 == 0:
            median = (nums1[len_spis // 2 - 1] + nums1[len_spis // 2 ]) / 2
            return median
        return nums1[len_spis // 2 ] / 1


"""TESTS:
1)Runtime 101 ms
Beats 88.18%
Memory 14.1 MB
Beats 97.6%
2)Runtime
221 ms
Beats 37.60%
Memory 14.1 MB
Beats 97.6%"""