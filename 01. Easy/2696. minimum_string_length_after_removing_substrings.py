class Solution:
    def minLength(self, s: str) -> int:

        while True:
            if 'AB' in s:
                s = s.replace('AB', '')
            elif 'CD' in s:
                s = s.replace('CD', '')
            else:
                break

        return len(s)


sol = Solution()
print(sol.minLength(s="ABFCACDB"))
print(sol.minLength(s="ACBBD"))

# Problem - https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/
