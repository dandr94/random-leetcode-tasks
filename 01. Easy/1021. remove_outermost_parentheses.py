class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''
        stack = []
        temp = ''

        for p in s:
            if p == '(':
                stack.append(p)
            else:
                stack.pop()

            temp += p

            if not stack:
                res += temp[1:-1]
                temp = ''

        return res


sol = Solution()
print(sol.removeOuterParentheses(s="(()())(())"))
print(sol.removeOuterParentheses(s="(()())(())(()(()))"))
print(sol.removeOuterParentheses(s="()()"))

# Problem - https://leetcode.com/problems/remove-outermost-parentheses/description/
