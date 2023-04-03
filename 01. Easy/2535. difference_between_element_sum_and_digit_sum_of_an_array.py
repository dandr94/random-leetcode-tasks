from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            while num:
                digit_sum += num % 10
                num //= 10

        return elem_sum - digit_sum


sol = Solution()
print(sol.differenceOfSum(nums=[1, 15, 6, 3]))
print(sol.differenceOfSum(nums=[1, 2, 3, 4]))
