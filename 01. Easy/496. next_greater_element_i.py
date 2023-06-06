from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = []
        #
        # for num in nums1:
        #     next_idx = nums2.index(num)
        #     for j in range(next_idx, len(nums2)):
        #         if nums2[j] > num:
        #             res.append(nums2[j])
        #             break
        #     else:
        #         res.append(-1)
        #
        # return res

        next_greater = {x: -1 for x in nums1}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                prev_num = stack.pop()
                if prev_num in next_greater:
                    next_greater[prev_num] = num

            stack.append(num)

        return [next_greater[x] for x in nums1]


sol = Solution()
print(sol.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(sol.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))

# Problem - https://leetcode.com/problems/next-greater-element-i/
