from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []

        for num in arr2:
            while num in arr1:
                arr1.remove(num)
                res.append(num)

        return res + sorted(arr1)


sol = Solution()
print(sol.relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
print(sol.relativeSortArray(arr1=[28, 6, 22, 8, 44, 17], arr2=[22, 28, 8, 6]))

# Problem - https://leetcode.com/problems/relative-sort-array/
