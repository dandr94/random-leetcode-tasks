class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0

        if s == s[::-1]:
            return 1

        return 2


sol = Solution()
print(sol.removePalindromeSub(s="ababa"))
print(sol.removePalindromeSub(s="abb"))
print(sol.removePalindromeSub(s="baabb"))

# Problem - https://leetcode.com/problems/remove-palindromic-subsequences/description/
