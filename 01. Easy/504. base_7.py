class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        _num = abs(num)
        res = ''

        while _num != 0:
            remainder = _num % 7
            _num //= 7
            res += str(remainder)

        return res[::-1] if num > 0 else "-" + res[::-1]


sol = Solution()
print(sol.convertToBase7(num=100))
print(sol.convertToBase7(num=-7))

# Problem - https://leetcode.com/problems/base-7/
