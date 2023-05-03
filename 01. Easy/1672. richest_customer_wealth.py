from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(i) for i in accounts)


sol = Solution()
print(sol.maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]))
print(sol.maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]]))
print(sol.maximumWealth(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]]))

# Problem - https://leetcode.com/problems/richest-customer-wealth/description/
