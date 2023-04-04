class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_end = len(s) - 1
        while last_word_end > 0 and s[last_word_end] == " ":
            last_word_end -= 1
        last_word_start = last_word_end
        while last_word_start >= 0 and s[last_word_start] != " ":
            last_word_start -= 1
        return last_word_end - last_word_start

        # return len(s.split()[-1])


sol = Solution()
print(sol.lengthOfLastWord(s="Hello World"))
print(sol.lengthOfLastWord(s="   fly me   to   the moon  "))
print(sol.lengthOfLastWord(s="luffy is still joyboy"))

# Problem - https://leetcode.com/problems/length-of-last-word/description/
