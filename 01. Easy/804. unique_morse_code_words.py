from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if len(words) == 1:
            return 1

        morse_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                          "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        _set = set()

        for word in words:
            morse = ''
            for letter in word:
                morse += morse_alphabet[ord(letter) - ord('a')]

            _set.add(morse)

        return len(_set)


sol = Solution()
print(sol.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"]))
print(sol.uniqueMorseRepresentations(words=["a"]))

# Problem - https://leetcode.com/problems/unique-morse-code-words/description/
