class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        idx = word.index(ch)

        prefix = word[:idx + 1][::-1]
        suffix = word[idx + 1:]

        return prefix + suffix


sol = Solution()
print(sol.reversePrefix(word="abcdefd", ch="d"))
print(sol.reversePrefix(word="xyxzxe", ch="z"))
print(sol.reversePrefix(word="abcd", ch="z"))

# Problem - https://leetcode.com/problems/reverse-prefix-of-word/
