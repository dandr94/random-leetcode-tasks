from collections import Counter


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0

        return sum(word * i in sequence for i in range(1, 101))


sol = Solution()
print(sol.maxRepeating(sequence="ababc", word="ab"))
print(sol.maxRepeating(sequence="ababc", word="ba"))
print(sol.maxRepeating(sequence="ababc", word="ac"))

# Problem - https://leetcode.com/problems/maximum-repeating-substring/
