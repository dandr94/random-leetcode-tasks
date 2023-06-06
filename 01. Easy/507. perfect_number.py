class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 3 or num % 2 != 0:
            return False

        divisors_sum = 1

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors_sum += i + (num // i)

        return divisors_sum == num


sol = Solution()
print(sol.checkPerfectNumber(num=28))
print(sol.checkPerfectNumber(num=7))

# Problem - https://leetcode.com/problems/perfect-number/
