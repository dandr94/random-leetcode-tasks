from typing import List
from collections import Counter


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums_amount = Counter(nums).most_common()

        return nums_amount[0][0]

        # set_nums = set(nums)
        # return (sum(nums) - sum(set_nums)) // (len(nums) - len(set_nums))


sol = Solution()
print(sol.repeatedNTimes(nums=[1, 2, 3, 3]))
print(sol.repeatedNTimes(nums=[2, 1, 2, 5, 3, 2]))
print(sol.repeatedNTimes(nums=[5, 1, 5, 2, 5, 3, 5, 4]))

# Problem - https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
