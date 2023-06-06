class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


sol = Solution()
print(sol.detectCapitalUse(word="USA"))
print(sol.detectCapitalUse(word="FlaG"))

# Problem - https://leetcode.com/problems/detect-capital/
