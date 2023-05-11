class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0


sol = Solution()
print(sol.isPowerOfThree(n=27))
print(sol.isPowerOfThree(n=0))
print(sol.isPowerOfThree(n=-1))

# Problem - https://leetcode.com/problems/power-of-three/
