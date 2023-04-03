from collections import defaultdict


class Solution:
    def countDigits(self, num: int) -> int:
        c = 0

        for i in str(num):
            if num % int(i) == 0:
                c += 1

        return c

        # c = 0
        #
        # t, tnum = 0, num
        # while num:
        #     t = num % 10
        #     num //= 10
        #
        #     if tnum % t == 0:
        #         c += 1
        #
        # return c


sol = Solution()
print(sol.countDigits(num=7))
print(sol.countDigits(num=121))
print(sol.countDigits(num=1248))

# Problem - https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
