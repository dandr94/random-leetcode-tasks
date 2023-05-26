from typing import List
from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        mapping = Counter(s1.split() + s2.split())

        return [x for x in mapping.keys() if mapping[x] == 1]

        


sol = Solution()
print(sol.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))
print(sol.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))


# Problem - https://leetcode.com/problems/uncommon-words-from-two-sentences/description/