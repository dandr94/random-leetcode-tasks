from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        tasks_dict, days = {}, 0
        for task in tasks:
            days += 1
            if task in tasks_dict and days - tasks_dict[task] <= space:
                days += space - (days - tasks_dict[task]) + 1
            tasks_dict[task] = days
        return days


sol = Solution()
print(sol.taskSchedulerII(tasks=[1, 2, 1, 2, 3, 1], space=3))
print(sol.taskSchedulerII(tasks=[5, 8, 8, 5], space=2))

# Problem - https://leetcode.com/problems/task-scheduler-ii/description/
