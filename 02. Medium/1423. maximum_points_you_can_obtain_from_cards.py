from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = sum(cardPoints[:k])
        res = s
        for i in range(1, k + 1):
            s += cardPoints[-i] - cardPoints[k - i]
            res = max(res, s)
        return res


sol = Solution()
print(sol.maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
print(sol.maxScore(cardPoints=[2, 2, 2], k=2))
print(sol.maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7))

# Problem - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
