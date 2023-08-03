from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        _len = len(nums)
        len_distinct_elements = len(set(nums))
        res = 0
        for i in range(_len):
            subarr_set = set()

            for j in range(i, _len):
                subarr_set.add(nums[j])

                if len(subarr_set) == len_distinct_elements:
                    res += 1

        return res


sol = Solution()
print(sol.countCompleteSubarrays(nums=[1, 3, 1, 2, 2]))
print(sol.countCompleteSubarrays(nums=[5, 5, 5, 5]))

# Problem - https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/
