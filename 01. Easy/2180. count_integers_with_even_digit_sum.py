class Solution:
    def countEven(self, num: int) -> int:
        n, digit_sum = num, 0

        while n > 0:
            digit_sum += n % 10
            n = n // 10

        return num // 2 - 1 if num % 2 == 0 and digit_sum % 2 == 1 else num // 2


sol = Solution()
print(sol.countEven(num=4))
print(sol.countEven(num=30))

# Problem - https://leetcode.com/problems/count-integers-with-even-digit-sum/description/
