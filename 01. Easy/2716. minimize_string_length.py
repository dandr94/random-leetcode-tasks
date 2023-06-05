class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))


sol = Solution()
print(sol.minimizedStringLength(s = "aaabc"))
print(sol.minimizedStringLength(s = "cbbd"))
print(sol.minimizedStringLength(s = "dddaaa"))

# Problem - https://leetcode.com/contest/weekly-contest-348/problems/minimize-string-length/