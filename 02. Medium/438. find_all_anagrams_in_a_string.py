from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char_amount = Counter(p)
        res = []
        left_idx = 0

        for right_idx, char in enumerate(s):
            char_amount[char] -= 1

            while char_amount[char] < 0:
                char_amount[s[left_idx]] += 1
                left_idx += 1

            if right_idx - left_idx + 1 == len(p):
                res.append(left_idx)

        return res


sol = Solution()
print(sol.findAnagrams(s="cbaebabacd", p="abc"))
print(sol.findAnagrams(s="abab", p="ab"))
print(sol.findAnagrams(s="aa", p="bb"))

# Problem - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
