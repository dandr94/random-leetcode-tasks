class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = [x.upper() for x in s if x != '-']

        amount_prefix = len(s) % k

        res = s[:amount_prefix]

        for i in range(amount_prefix, len(s), k):
            if res:
                res += '-'

            res += s[i: i + k]


        return "".join(res)

sol = Solution()
print(sol.licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4))
print(sol.licenseKeyFormatting(s = "2-5g-3-J", k = 2))


# Problem - https://leetcode.com/problems/license-key-formatting/