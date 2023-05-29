from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c, curr = 0, 0


        for num in nums:
            if num == 0:
                c = max(c, curr)
                curr = 0
            else:
                curr += 1

        return c if c > curr else curr


sol = Solution()
print(sol.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
print(sol.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))


# Problem - https://leetcode.com/problems/max-consecutive-ones/