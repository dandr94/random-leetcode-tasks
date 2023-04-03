from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        def solve(arr):
            res, count, flag = 0, 0, False
            for fort in arr:
                if fort == 1:
                    count = 0
                    flag = True
                elif fort == -1:
                    res = max(res, count)
                    count = 0
                    flag = False
                else:
                    if flag:
                        count += 1
            return res

        return max(solve(forts), solve(forts[::-1]))


sol = Solution()
print(sol.captureForts(forts=[1, 0, 0, -1, 0, 0, 0, 0, 1]))
print(sol.captureForts(forts=[0, 0, 1, -1]))

# Problem - https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/description/
