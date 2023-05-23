class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        _list = list(s)

        for i in range(len(s) // 2):
            if ord(_list[i]) > ord(_list[-i - 1]):
                _list[i] = _list[-i - 1]
            else:
                _list[-i - 1] = _list[i]

        return "".join(_list)


sol = Solution()
print(sol.makeSmallestPalindrome(s="egcfe"))
print(sol.makeSmallestPalindrome(s="abcd"))
print(sol.makeSmallestPalindrome(s="seven"))

# Problem - https://leetcode.com/problems/lexicographically-smallest-palindrome/description/
