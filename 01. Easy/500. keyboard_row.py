from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set('qwertyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')

        res = []

        for word in words:
            word_set = set(word.lower())
            if word_set <= first_row or word_set <= second_row or word_set <= third_row:
                res.append(word)

        return res


sol = Solution()
print(sol.findWords(words=["Hello", "Alaska", "Dad", "Peace"]))
print(sol.findWords(words=["omk"]))

# Problem - https://leetcode.com/problems/keyboard-row/
