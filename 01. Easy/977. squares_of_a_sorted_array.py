from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        :return: A new list containing the squares of each element in `nums`, sorted in non-decreasing order.
        """
        # One-line solution using list comprehension and sorting
        # return sorted(x ** 2 for x in nums)

        # Two-pointer approach
        res = []
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1

        # The result list needs to be reversed since we added elements from right to left
        return res[::-1]


sol = Solution()
print(sol.sortedSquares(nums=[-4, -1, 0, 3, 10]))
print(sol.sortedSquares(nums=[-7, -3, 2, 3, 11]))

# Problem - https://leetcode.com/problems/squares-of-a-sorted-array/
