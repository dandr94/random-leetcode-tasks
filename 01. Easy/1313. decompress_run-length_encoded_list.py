from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []

        for pair in range(0, len(nums), 2):
            freq = nums[pair]
            val = nums[pair + 1]

            res += [val] * freq

        return res


sol = Solution()
print(sol.decompressRLElist(nums=[1, 2, 3, 4]))
print(sol.decompressRLElist(nums=[1, 1, 2, 3]))

# Problem - https://leetcode.com/problems/decompress-run-length-encoded-list/
