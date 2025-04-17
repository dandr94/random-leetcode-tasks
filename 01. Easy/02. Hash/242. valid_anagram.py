from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


sol = Solution()
print(sol.isAnagram(s="anagram", t="nagaram"))
print(sol.isAnagram(s="rat", t="car"))

# Easy
# https://leetcode.com/problems/valid-anagram/description/
