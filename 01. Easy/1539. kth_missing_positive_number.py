from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] - mid <= k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k


sol = Solution()
print(sol.findKthPositive(arr=[2, 3, 4, 7, 11], k=5))
print(sol.findKthPositive(arr=[1, 2, 3, 4], k=2))

# Problem - https://leetcode.com/problems/kth-missing-positive-number/description/
