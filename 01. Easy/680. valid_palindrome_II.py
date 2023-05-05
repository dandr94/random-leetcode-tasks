class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(s, left, right, deletion):
            while left < right:
                if s[left] != s[right]:
                    if deletion == 1:
                        return False
                    else:
                        return is_pal(s, left + 1, right, deletion + 1) or is_pal(s, left, right - 1, deletion + 1)
                else:
                    left += 1
                    right -= 1

            return True

        return is_pal(s, 0, len(s) - 1, 0)


sol = Solution()
print(sol.validPalindrome(s="aba"))
print(sol.validPalindrome(s="abca"))
print(sol.validPalindrome(s="abc"))

# Problem - https://leetcode.com/problems/valid-palindrome-ii/description/