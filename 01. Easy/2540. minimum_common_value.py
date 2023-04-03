from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums1) & set(nums2)

        return min(s, default=-1)


sol = Solution()
print(sol.getCommon(nums1=[1, 2, 3], nums2=[2, 4]))
print(sol.getCommon(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]))

# Problem - https://leetcode.com/problems/minimum-common-value/
