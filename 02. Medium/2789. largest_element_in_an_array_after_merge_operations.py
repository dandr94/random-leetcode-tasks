from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        curr = 0
        _max = 0

        for num in nums[::-1]:
            if curr >= num:
                curr += num
            else:
                curr = num

            if curr >= _max:
                _max = curr

        return _max


sol = Solution()
print(sol.maxArrayValue(nums=[2, 3, 7, 9, 3]))
print(sol.maxArrayValue(nums=[5, 3, 3]))

# Problem - https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/description/
