from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []

        for word in words:
            _split = word.split(separator)
            for s in _split:
                if s == '':
                    continue
                res.append(s)

        return res


sol = Solution()
print(sol.splitWordsBySeparator(words = ["one.two.three","four.five","six"], separator = "."))
print(sol.splitWordsBySeparator(words = ["$easy$","$problem$"], separator = "$"))
print(sol.splitWordsBySeparator(words = ["|||"], separator = "|"))

# Problem - https://leetcode.com/problems/split-strings-by-separator/description/