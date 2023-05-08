from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, current_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < current_temp:
                prev_idx = stack.pop()
                res[prev_idx] = idx - prev_idx

            stack.append(idx)

        return res


sol = Solution()
print(sol.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
print(sol.dailyTemperatures(temperatures=[30, 40, 50, 60]))
print(sol.dailyTemperatures(temperatures=[30, 60, 90]))

# Problem - https://leetcode.com/problems/daily-temperatures/
