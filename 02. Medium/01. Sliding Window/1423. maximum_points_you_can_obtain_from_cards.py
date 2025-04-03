from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # total = sum(cardPoints)
        # n = len(cardPoints)
        # window_size = n - k
        # current_sum = sum(cardPoints[:window_size])
        # min_sum_to_remove = current_sum
        #
        # for i in range(window_size, n):
        #     current_sum += cardPoints[i] - cardPoints[i - window_size]
        #     min_sum_to_remove = min(min_sum_to_remove, current_sum)
        #
        # return total - min_sum_to_remove

        current_sum = sum(cardPoints[:k])
        max_score = current_sum

        for i in range(1, k + 1):
            current_sum += cardPoints[-i] - cardPoints[k - i]
            max_score = max(max_score, current_sum)

        return max_score


sol = Solution()
print(sol.maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
print(sol.maxScore(cardPoints=[2, 2, 2], k=2))
print(sol.maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7))

# Medium
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
