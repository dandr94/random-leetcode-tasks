class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_of_digits = 0
        product_of_digits = 1

        while n != 0:
            sum_of_digits += n % 10
            product_of_digits *= n % 10
            n //= 10

        return product_of_digits - sum_of_digits


sol = Solution()
print(sol.subtractProductAndSum(n=234))
print(sol.subtractProductAndSum(n=4421))

# Problem - https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
