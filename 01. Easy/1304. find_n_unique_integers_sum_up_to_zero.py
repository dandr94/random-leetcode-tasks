from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []

        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)

        if n % 2 != 0:
            res.append(0)

        return res


sol = Solution()
print(sol.sumZero(n=5))
print(sol.sumZero(n=3))
print(sol.sumZero(n=1))

# Problem - https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
