from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        :return: A new list where each element represents the number of smaller elements of that
                    element in the original list.
        """
        # res = []
        #
        # for i in range(len(nums)):
        #     left = 0
        #     right = len(nums) - 1
        #     count = 0
        #
        #     while left < i:
        #         if nums[left] < nums[i]:
        #             count += 1
        #         left += 1
        #
        #     while right > i:
        #         if nums[right] < nums[i]:
        #             count += 1
        #
        #         right -= 1
        #
        #     res.append(count)
        #
        # return res
        mapping = {}
        for idx, num in enumerate(sorted(nums)):
            if num not in mapping:
                mapping[num] = idx
        return [mapping[num] for num in nums]


sol = Solution()
print(sol.smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]))
print(sol.smallerNumbersThanCurrent(nums=[6, 5, 4, 8]))
print(sol.smallerNumbersThanCurrent(nums=[7, 7, 7, 7]))

# Problem - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
