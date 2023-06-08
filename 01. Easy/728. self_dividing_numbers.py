from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(left, right + 1):
            nums = list(str(i))

            if '0' in nums:
                continue

            self_dividing = [x for x in nums if i % int(x) == 0]

            if len(self_dividing) == len(nums):
                res.append(i)

        return res


sol = Solution()
print(sol.selfDividingNumbers(left=1, right=22))
print(sol.selfDividingNumbers(left=47, right=85))

# Problem - https://leetcode.com/problems/self-dividing-numbers/
