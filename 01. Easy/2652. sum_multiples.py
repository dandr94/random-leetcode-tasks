class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum([x for x in range(1, n + 1) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0])


sol = Solution()
print(sol.sumOfMultiples(n=7))
print(sol.sumOfMultiples(n=10))
print(sol.sumOfMultiples(n=9))

# Problem - https://leetcode.com/problems/sum-multiples/
