import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n, 4).is_integer()
    

sol = Solution()

print(sol.isPowerOfFour(n=16))
print(sol.isPowerOfFour(n=5))
print(sol.isPowerOfFour(n=1))

# Problem - https://leetcode.com/problems/power-of-four/description/