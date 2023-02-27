from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        x = ''
        for i in words:
            if i not in s:
                return False
            x += i

            if x == s:
                return True


sol = Solution()
print(sol.isPrefixString(s="iloveleetcode", words=["i", "love", "leetcode", "apples"]))
print(sol.isPrefixString(s="iloveleetcode", words=["apples", "i", "love", "leetcode"]))

# Problem - https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/description/
