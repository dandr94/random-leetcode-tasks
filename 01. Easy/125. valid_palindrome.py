class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [x for x in s.lower() if x.isalnum()]

        return x[::] == x[::-1]


sol = Solution()
print(sol.isPalindrome(s="A man, a plan, a canal: Panama"))
print(sol.isPalindrome(s="race a car"))
print(sol.isPalindrome(s=" "))

# Problem - https://leetcode.com/problems/valid-palindrome/
