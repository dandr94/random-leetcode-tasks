from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """
        :return: The largest lucky integer found in the list. If there are no lucky integers, it returns -1.
                    A lucky integer is an integer that has the same value as its frequency in the list.
        """
        mapping = Counter(arr)

        res = -1
        for k, v in mapping.items():
            if k == v:
                res = max(k, res)

        return res


sol = Solution()
print(sol.findLucky(arr=[2, 2, 3, 4]))
print(sol.findLucky(arr=[1, 2, 2, 3, 3, 3]))
print(sol.findLucky(arr=[2, 2, 2, 3, 3]))

# Problem - https://leetcode.com/problems/find-lucky-integer-in-an-array/
