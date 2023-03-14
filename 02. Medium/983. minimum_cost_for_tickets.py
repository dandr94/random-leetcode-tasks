from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day_travel = days[-1]
        days_set = set(days)
        dp = [0 for _ in range(last_day_travel + 1)]

        for day in range(1, last_day_travel + 1):
            if day not in days_set:
                dp[day] = dp[day - 1]
                continue

            with_1_day_pass = dp[day - 1] + costs[0]
            with_7_day_pass = dp[max(day - 7, 0)] + costs[1]
            with_30_day_pass = dp[max(day - 30, 0)] + costs[2]

            dp[day] = min(with_1_day_pass, with_7_day_pass, with_30_day_pass)

        return dp[-1]


sol = Solution()
print(sol.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
print(sol.mincostTickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]))

# Problem - https://leetcode.com/problems/minimum-cost-for-tickets/description/
