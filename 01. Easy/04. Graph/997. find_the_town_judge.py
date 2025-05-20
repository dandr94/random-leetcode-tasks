from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_scores = [0] * (n + 1)

        for a, b in trust:
            trust_scores[a] -= 1
            trust_scores[b] += 1

        for person in range(1, n + 1):
            if trust_scores[person] == n - 1:
                return person

        return -1


sol = Solution()

print(sol.findJudge(n=2, trust=[[1, 2]]))

print(sol.findJudge(n=3, trust=[[1, 3], [2, 3]]))

print(sol.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))

# Easy
# https://leetcode.com/problems/find-the-town-judge/description/
