from typing import List
from collections import deque


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = deque()

        for num in nums[::-1]:
            while num:
                res.appendleft(num % 10)
                num //= 10

        return res


sol = Solution()
print(sol.separateDigits(nums=[13, 25, 83, 77]))
print(sol.separateDigits(nums=[7, 1, 3, 9]))

# Problem - https://leetcode.com/problems/separate-the-digits-in-an-array/
