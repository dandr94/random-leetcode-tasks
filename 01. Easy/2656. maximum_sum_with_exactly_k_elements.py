from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return sum([max(nums) + x for x in range(k)])


sol = Solution()
print(sol.maximizeSum(nums=[1, 2, 3, 4, 5], k=3))
print(sol.maximizeSum(nums=[5, 5, 5], k=2))

# Problem - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/
