from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_dict = {x: y for y, x in enumerate(score)}

        x = sorted(score, key=lambda x: x, reverse=True)

        for i in range(len(x)):
            curr_index = score_dict[x[i]]
            if i == 0:
                score[curr_index] = 'Gold Medal'
            elif i == 1:
                score[curr_index] = 'Silver Medal'
            elif i == 2:
                score[curr_index] = 'Bronze Medal'
            else:
                score[score_dict[x[i]]] = str(i + 1)

        return score


sol = Solution()
print(sol.findRelativeRanks(score=[5, 4, 3, 2, 1]))
print(sol.findRelativeRanks(score=[10, 3, 8, 9, 4]))

# Problem - https://leetcode.com/problems/relative-ranks/description/
