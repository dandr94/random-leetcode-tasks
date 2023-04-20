class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for l in s:
            if stack and stack[-1] == l.swapcase():
                stack.pop()
            else:
                stack.append(l)

        return "".join(stack)

sol = Solution()
print(sol.makeGood(s="leEeetcode"))
print(sol.makeGood(s="abBAcC"))
print(sol.makeGood(s="s"))

# Problem - https://leetcode.com/problems/make-the-string-great/
