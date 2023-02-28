from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((w for w in words if w == w[:: -1]), '')


sol = Solution()
print(sol.firstPalindrome(words=["abc", "car", "ada", "racecar", "cool"]))
print(sol.firstPalindrome(words=["notapalindrome", "racecar"]))
print(sol.firstPalindrome(words=["def", "ghi"]))

# Problem - https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
