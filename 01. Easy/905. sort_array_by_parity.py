from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # even = []
        # odd = []

        # for num in nums:
        #     if num % 2 == 0:
        #         even.append(num)
        #     else:
        #         odd.append(num)

        # return even + odd

        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        
        return nums

sol = Solution()
print(sol.sortArrayByParity(nums = [3,1,2,4]))
print(sol.sortArrayByParity(nums = [0]))

# Problem - https://leetcode.com/problems/sort-array-by-parity/