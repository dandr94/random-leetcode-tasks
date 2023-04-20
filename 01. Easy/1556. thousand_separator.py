from collections import deque


class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)

        res = deque()

        for idx, num in enumerate(str(n)[::-1]):
            if idx % 3 == 0 and idx != 0:
                res.appendleft('.')

            res.appendleft(num)

        return ''.join(res)


sol = Solution()
print(sol.thousandSeparator(n=987))
print(sol.thousandSeparator(n=1234))

# Problem - https://leetcode.com/problems/thousand-separator/description/
