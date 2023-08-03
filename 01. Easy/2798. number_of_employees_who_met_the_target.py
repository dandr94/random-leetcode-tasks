from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return len([x for x in hours if x >= target])


sol = Solution()
print(sol.numberOfEmployeesWhoMetTarget(hours=[0, 1, 2, 3, 4], target=2))
print(sol.numberOfEmployeesWhoMetTarget(hours=[5, 1, 4, 2, 2], target=6))

# Problem - https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
