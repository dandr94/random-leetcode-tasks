from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        res = i = best = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                best = max(jobs[i][1], best)
                i += 1
            res += best
        return res


sol = Solution()
print(sol.maxProfitAssignment(difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50], worker=[4, 5, 6, 7]))
print(sol.maxProfitAssignment(difficulty=[85, 47, 57], profit=[24, 66, 99], worker=[40, 25, 25]))

# Problem - https://leetcode.com/problems/most-profit-assigning-work/description/
