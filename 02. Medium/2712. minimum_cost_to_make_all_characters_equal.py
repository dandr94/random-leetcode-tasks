class Solution:
    def minimumCost(self, s: str) -> int:
        res = 0

        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                res += min(i, len(s) - i)

        return res



sol = Solution()
print(sol.minimumCost(s = "0011"))
print(sol.minimumCost(s = "010101"))

# Problem - https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/description/