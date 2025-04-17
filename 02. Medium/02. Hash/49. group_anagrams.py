from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = {}
        # res = []
        #
        # for chars in strs:
        #     sorted_chars = tuple(sorted(chars))
        #
        #     if sorted_chars in anagrams:
        #         res[anagrams[sorted_chars]].append(chars)
        #     else:
        #         res.append([chars])
        #         anagrams[sorted_chars] = len(res) - 1
        #
        # return res

        anagrams = defaultdict(list)

        for chars in strs:
            sorted_chars = tuple(sorted(chars))
            anagrams[sorted_chars].append(chars)

        return list(anagrams.values())


sol = Solution()
print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(sol.groupAnagrams(strs=[""]))
print(sol.groupAnagrams(strs=["a"]))

# Medium
# https://leetcode.com/problems/group-anagrams/description/
