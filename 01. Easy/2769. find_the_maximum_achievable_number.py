class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


sol = Solution()
print(sol.theMaximumAchievableX(num=4, t=1))
print(sol.theMaximumAchievableX(num=3, t=2))

# Problem - https://leetcode.com/problems/find-the-maximum-achievable-number/description/
