from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        rows = len(nums)

        for row in range(rows):
            nums[row] = sorted(nums[row])

        _sum = 0
        while nums[rows - 1]:
            biggest_number_in_row = set()
            for i in range(rows):
                biggest_number_in_row.add(nums[i].pop())

            _sum += max(biggest_number_in_row)

        return _sum


sol = Solution()
print(sol.matrixSum(nums=[[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]))
print(sol.matrixSum(nums=[[1]]))

# Problem - https://leetcode.com/problems/sum-in-a-matrix/description/
