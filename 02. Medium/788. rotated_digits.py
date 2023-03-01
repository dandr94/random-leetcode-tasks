class Solution:
    def rotatedDigits(self, n: int) -> int:
        c = 0
        for num in range(2, n + 1):
            number = f'{num}'
            if '3' in number or '7' in number or '4' in number:
                continue
            if '2' in number or '5' in number or '6' in number or '9' in number:
                c += 1
        return c


sol = Solution()
print(sol.rotatedDigits(n=10))
print(sol.rotatedDigits(n=1))
print(sol.rotatedDigits(n=2))


# Problem - https://leetcode.com/problems/rotated-digits/
