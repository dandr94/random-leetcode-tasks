class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # return num.rstrip('0')

        if num[-1] == '0':
            for idx, n in enumerate(num[::-1]):
                if n != '0':
                    return num[:-idx]
        else:
            return num


sol = Solution()
print(sol.removeTrailingZeros(num = "51230100"))
print(sol.removeTrailingZeros(num = "123"))


# Problem - https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/