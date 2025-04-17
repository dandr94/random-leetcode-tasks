from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], idx]

            seen[num] = idx

        return []


sol = Solution()
print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
print(sol.twoSum(nums=[3, 2, 4], target=6))
print(sol.twoSum(nums=[3, 3], target=6))

# Easy
# https://leetcode.com/problems/two-sum/
