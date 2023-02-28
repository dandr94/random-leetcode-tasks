from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        return (Counter(nums1) & Counter(nums2)).elements()


sol = Solution()
print(sol.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(sol.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))

# Problem - https://leetcode.com/problems/intersection-of-two-arrays-ii/description/