class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))


sol = Solution()
print(sol.minimizedStringLength(s="aaabc"))
print(sol.minimizedStringLength(s="cbbd"))
print(sol.minimizedStringLength(s="dddaaa"))

# https://leetcode.com/problems/minimize-string-length/description/
