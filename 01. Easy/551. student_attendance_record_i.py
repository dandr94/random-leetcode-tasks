class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s


sol = Solution()
print(sol.checkRecord(s="PPALLP"))
print(sol.checkRecord(s="PPALLL"))

# Problem - https://leetcode.com/problems/student-attendance-record-i/description/
