from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_len = 0
        delete_used = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                delete_used += 1

            while delete_used > 1:
                if nums[left] == 0:
                    delete_used -= 1

                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len - 1


sol = Solution()
print(sol.longestSubarray(nums=[1, 1, 0, 1]))
print(sol.longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(sol.longestSubarray(nums=[1, 1, 1]))

# Medium
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
