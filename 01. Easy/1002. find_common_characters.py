from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        check = list(words[0])
        for word in words[1:]:
            new_check = []
            for letter in word:
                if letter in check:
                    new_check.append(letter)
                    check.remove(letter)
            check = new_check

        return check


sol = Solution()
print(sol.commonChars(words=["bella", "label", "roller"]))
print(sol.commonChars(words=["cool", "lock", "cook"]))

# Problem - https://leetcode.com/problems/find-common-characters/description/
