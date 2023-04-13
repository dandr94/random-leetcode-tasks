class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)

        c, i = 0, 0
        while i < len(num_str) - k + 1:
            n = num_str[i:i + k]

            if int(n) and num % int(n) == 0:
                c += 1

            i += 1

        return c


sol = Solution()
print(sol.divisorSubstrings(num=240, k=2))
print(sol.divisorSubstrings(num=430043, k=2))

# Problem - https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/
