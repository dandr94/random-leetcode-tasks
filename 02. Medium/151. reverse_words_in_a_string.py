class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


sol = Solution()
print(sol.reverseWords(s="the sky is blue"))
print(sol.reverseWords(s="  hello world  "))
print(sol.reverseWords(s="a good   example"))

# Problem - https://leetcode.com/problems/reverse-words-in-a-string/
