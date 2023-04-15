class Solution:
    def minimumSum(self, num: int) -> int:
        _sorted = sorted(str(num))

        return int(_sorted[0] + _sorted[2]) + int(_sorted[1] + _sorted[3])


sol = Solution()
print(sol.minimumSum(num=2932))
print(sol.minimumSum(num=4009))

# Problem - https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/
