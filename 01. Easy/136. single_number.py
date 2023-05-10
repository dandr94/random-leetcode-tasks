from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return reduce(lambda p, n: p ^ n, nums) XOR

        return Counter(nums).most_common()[-1][0]


sol = Solution()
print(sol.singleNumber(nums=[2, 2, 1]))
print(sol.singleNumber(nums=[4, 1, 2, 1, 2]))
print(sol.singleNumber(nums=[1]))

# Problem - https://leetcode.com/problems/single-number/description/
