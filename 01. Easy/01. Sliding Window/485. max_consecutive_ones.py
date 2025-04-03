from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_cons_ones = 0
        while right < len(nums):
            if nums[right] != 1:
                max_cons_ones = max(max_cons_ones, sum(nums[left:right]))
                left = right + 1
            right += 1

        max_cons_ones = max(max_cons_ones, sum(nums[left:right]))

        return max_cons_ones

        # Better solution without sum()
        # max_cons_ones = 0
        # count = 0
        #
        # for num in nums:
        #     if num == 1:
        #         count += 1
        #     else:
        #         max_cons_ones = max(max_cons_ones, count)
        #         count = 0
        #
        # max_cons_ones = max(max_cons_ones, count)


sol = Solution()
print(sol.findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1]))
print(sol.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1]))

# Easy
# https://leetcode.com/problems/max-consecutive-ones/description/
