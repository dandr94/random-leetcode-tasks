from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        if len(nums) == 1:
            return nums[0]

        col = Counter(nums)

        for key, value in col.items():
            if value == 1:
                return key

        # Bits

        # a = b = 0
        # for n in nums:
        #     b = (b ^ n) & ~a
        #     a = (a ^ n) & ~b
        # return b


sol = Solution()
print(sol.singleNumber(nums=[2, 2, 3, 2]))
print(sol.singleNumber(nums=[0, 1, 0, 1, 0, 1, 99]))

# Problem - https://leetcode.com/problems/single-number-ii/description/
