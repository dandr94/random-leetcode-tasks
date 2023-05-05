class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # binary = bin(n)
        #
        # return '00' not in binary and '11' not in binary

        x = 1
        while x <= n:
            if x == n:
                return True
            elif x & 1:
                x = 2 * x
            else:
                x = 2 * x + 1

        return False


sol = Solution()
print(sol.hasAlternatingBits(n=5))
print(sol.hasAlternatingBits(n=7))
print(sol.hasAlternatingBits(n=11))

# Problem - https://leetcode.com/problems/binary-number-with-alternating-bits/description/
