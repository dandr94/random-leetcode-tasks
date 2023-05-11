from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))

        return res


sol = Solution()
print(sol.fizzBuzz(n=3))
print(sol.fizzBuzz(n=5))
print(sol.fizzBuzz(n=15))

# Problem - https://leetcode.com/problems/fizz-buzz/description/
