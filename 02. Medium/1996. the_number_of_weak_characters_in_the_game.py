from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        sorted_chars = sorted(properties, key=lambda x: (-x[0], x[1]))

        res = 0

        max_def = 0

        for char in sorted_chars:
            defense = char[1]

            if defense < max_def:
                res += 1
            else:
                max_def = defense

        return res


sol = Solution()
print(sol.numberOfWeakCharacters(properties=[[5, 5], [6, 3], [3, 6]]))
print(sol.numberOfWeakCharacters(properties=[[2, 2], [3, 3]]))
print(sol.numberOfWeakCharacters(properties=[[1, 5], [10, 4], [4, 3]]))

# Problem - https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
