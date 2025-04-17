from typing import List
from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # counter = Counter(nums)
        # for count in counter.values():
        #     if count > 1:
        #         return True
        # return False

        return len(set(nums)) != len(nums)


sol = Solution()
print(sol.containsDuplicate(nums=[1, 2, 3, 1]))
print(sol.containsDuplicate(nums=[1, 2, 3, 4]))
print(sol.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

# Easy
# https://leetcode.com/problems/contains-duplicate/
