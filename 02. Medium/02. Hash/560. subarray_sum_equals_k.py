from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        sum_dict = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in sum_dict:
                res += sum_dict[prefix_sum - k]

            sum_dict[prefix_sum] = sum_dict.get(prefix_sum, 0) + 1

        return res


sol = Solution()
print(sol.subarraySum(nums=[1, 1, 1], k=2))
print(sol.subarraySum(nums=[1, 2, 3], k=3))
print(sol.subarraySum(nums=[1], k=1))

# Medium
# https://leetcode.com/problems/subarray-sum-equals-k/
