class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(0, int(n**(1/2)) + 1)] 
		
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for square in squares:
            for i in range(1, n + 1):
                if i >= square:
                    dp[i] = min(dp[i], dp[i - square] + 1)
               
        return dp[-1]


sol = Solution()
print(sol.numSquares(n=12))
print(sol.numSquares(n=13))

# Problem - https://leetcode.com/problems/perfect-squares/