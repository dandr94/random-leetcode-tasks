from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)

        return list(set_1.intersection(set_2))
    

sol = Solution()
print(sol.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))

# Problem - https://leetcode.com/problems/intersection-of-two-arrays/description/