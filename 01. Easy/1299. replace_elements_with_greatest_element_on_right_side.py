from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1

        for i in range(len(arr) - 1, -1, -1):
            arr[i], curr_max = curr_max, max(arr[i], curr_max)

        return arr


sol = Solution()
print(sol.replaceElements(arr=[17, 18, 5, 4, 6, 1]))
print(sol.replaceElements(arr=[400]))

# Problem - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
