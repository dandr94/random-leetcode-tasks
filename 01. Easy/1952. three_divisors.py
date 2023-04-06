import math


class Solution:
    def isThree(self, n: int) -> bool:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

        return math.sqrt(n) in primes


sol = Solution()
print(sol.isThree(2))
print(sol.isThree(4))

# Problem - https://leetcode.com/problems/three-divisors/description/
