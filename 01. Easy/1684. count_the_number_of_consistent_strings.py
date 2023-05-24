from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        c = 0
        for word in words:
            _set = set(word)

            x = _set.difference(allowed_set)
            if not x:
                c += 1

        return c


sol = Solution()
print(sol.countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]))
print(sol.countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]))
print(sol.countConsistentStrings(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))

# Problem - https://leetcode.com/problems/count-the-number-of-consistent-strings/
