import re


class Solution:
    def freqAlphabets(self, s: str) -> str:
        regex = r'\d\d#|\d'

        x = ''
        for i in re.findall(regex, s):
            y = chr(int(i[:2]) + 96)
            x += y

        return x


sol = Solution()
print(sol.freqAlphabets(s="10#11#12"))
print(sol.freqAlphabets(s="1326#"))

# Problem - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/
