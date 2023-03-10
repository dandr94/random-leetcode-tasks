class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        s = s.replace('))', '}')
        open_bracket_count = 0

        for c in s:
            if c == '(':
                open_bracket_count += 1

            else:

                if c == ')':
                    count += 1

                if open_bracket_count:
                    open_bracket_count -= 1

                else:
                    count += 1

        return count + open_bracket_count * 2


sol = Solution()
print(sol.minInsertions(s="(()))"))
print(sol.minInsertions(s="())"))
print(sol.minInsertions(s="))())("))


# Problem - https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/?orderBy=most_votes