from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        _min = min(nums)
        _max = max(nums)

        return len([num for num in nums if _min < num < _max])


sol = Solution()
print(sol.countElements(nums=[11, 7, 2, 15]))
print(sol.countElements(nums=[-3, 3, 3, 90]))

# Problem - https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/
