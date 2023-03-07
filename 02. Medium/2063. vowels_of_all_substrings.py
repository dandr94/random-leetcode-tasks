class Solution:
    def countVowels(self, word: str) -> int:

        s = 0

        for i, w in enumerate(word):
            if w in 'aeiou':
                s += (i + 1) * (len(word) - i)

        return s


sol = Solution()
print(sol.countVowels(word="aba"))
print(sol.countVowels(word='abc'))
print(sol.countVowels(word="ltcd"))

# Problem - https://leetcode.com/problems/vowels-of-all-substrings/description/
