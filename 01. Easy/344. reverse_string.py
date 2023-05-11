from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


sol = Solution()
print(sol.reverseString(s=["h", "e", "l", "l", "o"]))
print(sol.reverseString(s=["H", "a", "n", "n", "a", "h"]))

# Problem -https://leetcode.com/problems/reverse-string/description/
