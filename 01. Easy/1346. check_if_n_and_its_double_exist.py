from collections import Counter
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        _dict = Counter(arr)
        return any(2 * x in _dict and (x != 2 * x or _dict[x] > 1) for x in arr)


sol = Solution()
print(sol.checkIfExist(arr=[10, 2, 5, 3]))
print(sol.checkIfExist(arr=[3, 1, 7, 11]))

# Problem - https://leetcode.com/problems/check-if-n-and-its-double-exist/description/