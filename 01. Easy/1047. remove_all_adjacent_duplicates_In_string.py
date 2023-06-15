class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []

        for l in s:
            if res and res[-1] == l:
                res.pop()
            else:
                res.append(l)

        return "".join(res)


sol = Solution()
print(sol.removeDuplicates(s="abbaca"))
print(sol.removeDuplicates(s="azxxzy"))

# Problem - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
