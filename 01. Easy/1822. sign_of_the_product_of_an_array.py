from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c = 0

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                c += 1

        return 1 if c % 2 == 0 else - 1


sol = Solution()
print(sol.arraySign(nums=[-1, -2, -3, -4, 3, 2, 1]))
print(sol.arraySign(nums=[1, 5, 0, 2, -3]))
print(sol.arraySign(nums=[-1, 1, -1, 1, -1]))

# Problem - https://leetcode.com/problems/sign-of-the-product-of-an-array/
