class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) > len(s):
            return False

        if s == goal:
            return True

        n = len(s)

        while n:
            s = s[1:] + s[0]

            if s == goal:
                return True
            n -= 1

        return False


sol = Solution()
print(sol.rotateString(s="abcde", goal="cdeab"))
print(sol.rotateString(s="abcde", goal="abced"))

# Problem - https://leetcode.com/problems/rotate-string/description/
