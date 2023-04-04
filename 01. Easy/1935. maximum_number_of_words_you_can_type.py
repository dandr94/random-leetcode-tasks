class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = set(brokenLetters)
        c = 0

        for word in text.split():
            if all(w not in s for w in word):
                c += 1

        return c


sol = Solution()
print(sol.canBeTypedWords(text="hello world", brokenLetters="ad"))
print(sol.canBeTypedWords(text="leet code", brokenLetters="lt"))
print(sol.canBeTypedWords(text="leet code", brokenLetters="e"))

# Problem - https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/
