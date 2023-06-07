from typing import List
from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        amount = Counter(arr).most_common()

        return amount[0][0]


sol = Solution()
print(sol.findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]))
print(sol.findSpecialInteger(arr=[1, 1]))

# Problem - https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
