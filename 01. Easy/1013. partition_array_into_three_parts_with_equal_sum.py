from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        target = sum(arr) / 3
        part_sum = 0
        count = 0
        for i in range(len(arr)):
            part_sum += arr[i]
            if part_sum == target:
                count += 1
                part_sum = 0
            if count == 3:
                return True
        return False


sol = Solution()
print(sol.canThreePartsEqualSum(arr=[0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
print(sol.canThreePartsEqualSum(arr=[0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
print(sol.canThreePartsEqualSum(arr=[3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))

# Problem - https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/
