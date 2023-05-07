class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        c = 1

        while c < n:
            c = c << 1 | 1

        return n ^ c


sol = Solution()
print(sol.bitwiseComplement(n=5))
print(sol.bitwiseComplement(n=7))
print(sol.bitwiseComplement(n=10))

# Problem - https://leetcode.com/problems/complement-of-base-10-integer/
