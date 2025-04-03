from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_cons_ones = 0
        k_used = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k_used += 1

            while k_used > k:
                if nums[left] == 0:
                    k_used -= 1

                left += 1

            max_cons_ones = max(max_cons_ones, right - left + 1)

        return max_cons_ones


sol = Solution()
print(sol.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(sol.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))

# Medium 
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
