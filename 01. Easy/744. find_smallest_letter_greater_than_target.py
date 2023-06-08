from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        mapped = [x for x in letters if ord(x) > ord(target)]

        return letters[0] if not mapped else mapped[0]


sol = Solution()
print(sol.nextGreatestLetter(letters=["c", "f", "j"], target="a"))
print(sol.nextGreatestLetter(letters=["c", "f", "j"], target="c"))
print(sol.nextGreatestLetter(letters=["x", "x", "y", "y"], target="z"))

# Problem - https://leetcode.com/problems/find-smallest-letter-greater-than-target/
