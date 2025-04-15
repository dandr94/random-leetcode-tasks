from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        max_in_windows = []

        left = 0

        for right in range(len(nums)):
            # Remove indices from the back if the current number is greater
            # Because they are smaller and no longer useful
            while window and nums[right] > nums[window[-1]]:
                window.pop()

            window.append(right)

            # Remove indices from the front if they’re out of the window range
            if window[0] < left:
                window.popleft()

            # Once the window has at least k elements, start recording maxes
            if right - left + 1 >= k:
                max_in_windows.append(nums[window[0]])
                left += 1

        return max_in_windows


sol = Solution()
print(sol.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(sol.maxSlidingWindow(nums=[1], k=1))

# Hard
# https://leetcode.com/problems/sliding-window-maximum/description/
