from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def generate(wordlist: List[str]):
            for word in wordlist:
                for char in word:
                    yield char
            yield None

        for c1, c2 in zip(generate(word1), generate(word2)):
            if c1 != c2:
                return False
        return True

        # return "".join(word1) == "".join(word2)


sol = Solution()
print(sol.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))
print(sol.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))
print(sol.arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]))

# Problem - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
