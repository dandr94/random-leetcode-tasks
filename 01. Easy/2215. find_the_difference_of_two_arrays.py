from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1).difference(nums2)

        s2 = set(nums2).difference(nums1)

        return [list(s1), list(s2)]


sol = Solution()
print(sol.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
print(sol.findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))

# Problem - https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
