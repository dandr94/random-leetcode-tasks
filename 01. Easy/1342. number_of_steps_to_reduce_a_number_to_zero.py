class Solution:
    def numberOfSteps(self, num: int) -> int:
        if not num:
            return 0

        res = 0

        while num:
            res += (num & 1) + 1
            num >>= 1

        return res - 1


sol = Solution()
print(sol.numberOfSteps(num=14))
print(sol.numberOfSteps(num=8))
print(sol.numberOfSteps(num=123))

# Problem - https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
