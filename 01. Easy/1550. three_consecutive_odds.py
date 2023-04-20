from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # for i in range(len(arr) - 2):
        #     if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
        #         return True
        #
        # return False

        # for i in range(len(arr) - 2):
        #     if arr[i] & 1 and arr[i + 1] & 1 and arr[i + 2] & 1:
        #         return True
        #
        # return False

        return '111' in "".join(str(i & 1) for i in arr)


sol = Solution()
print(sol.threeConsecutiveOdds(arr=[2, 6, 4, 1]))
print(sol.threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]))

# Problem - https://leetcode.com/problems/three-consecutive-odds/
