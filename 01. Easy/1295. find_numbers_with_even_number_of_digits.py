from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = [num for num in nums if len(str(num)) % 2 == 0]

        return len(res)


sol = Solution()
print(sol.findNumbers(nums=[12, 345, 2, 6, 7896]))
print(sol.findNumbers(nums=[555, 901, 482, 1771]))

# Problem - https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
