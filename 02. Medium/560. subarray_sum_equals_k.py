from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        _dict = {0: 1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in _dict:
                res = res + _dict[prefix_sum - k]
            _dict[prefix_sum] = _dict.get(prefix_sum, 0) + 1
        return res


sol = Solution()
print(sol.subarraySum(nums=[1, 1, 1], k=2))
print(sol.subarraySum(nums=[1, 2, 3], k=3))

# Problem - https://leetcode.com/problems/subarray-sum-equals-k/
