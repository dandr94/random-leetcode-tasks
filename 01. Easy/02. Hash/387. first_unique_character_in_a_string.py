from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for idx, ch in enumerate(s):
            if counter[ch] == 1:
                return idx

        return -1


sol = Solution()
print(sol.firstUniqChar(s="leetcode"))
print(sol.firstUniqChar(s="loveleetcode"))
print(sol.firstUniqChar(s="aabb"))

# Easy
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
