from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for i in range(1, len(words) + 1):
            if s == ''.join(words[:i]):
                return True
        return False


sol = Solution()
print(sol.isPrefixString(s="iloveleetcode", words=["i", "love", "leetcode", "apples"]))
print(sol.isPrefixString(s="iloveleetcode", words=["apples", "i", "love", "leetcode"]))

# Problem - https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/description/
