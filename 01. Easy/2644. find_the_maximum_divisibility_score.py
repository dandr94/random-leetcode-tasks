from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res = 0
        curr = -1

        for divisor in divisors:
            score = 0

            for num in nums:
                score += num % divisor == 0

            if score > curr:
                curr = score
                res = divisor
            elif score == curr:
                res = min(res, divisor)

        return res


sol = Solution()
print(sol.maxDivScore(nums=[4, 7, 9, 3, 9], divisors=[5, 2, 3]))
print(sol.maxDivScore(nums=[20, 14, 21, 10], divisors=[5, 7, 5]))
print(sol.maxDivScore(nums=[12], divisors=[10, 16]))

# Problem - https://leetcode.com/problems/find-the-maximum-divisibility-score/
