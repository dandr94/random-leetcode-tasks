class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber, r = divmod(columnNumber - 1, 26)
            res.append(chr(r + ord('A')))
        return "".join(res[::-1])


sol = Solution()
print(sol.convertToTitle(columnNumber=1))
print(sol.convertToTitle(columnNumber=28))
print(sol.convertToTitle(columnNumber=701))

# Problem - https://leetcode.com/problems/excel-sheet-column-title/description/
