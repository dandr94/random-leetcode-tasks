from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        nums.sort(reverse=True)

        for i in range(len(nums) - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]
            if a < b + c:
                return a + b + c
        return 0


sol = Solution()
print(sol.largestPerimeter(nums=[2, 1, 2]))
print(sol.largestPerimeter(nums=[1, 2, 1, 10]))

# Problem - https://leetcode.com/problems/largest-perimeter-triangle/description/
