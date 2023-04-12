class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        numbers = "".join(l if l.isdigit() else ' ' for l in word)
        res = set(int(x) for x in numbers.split())
        return len(res)


sol = Solution()
print(sol.numDifferentIntegers(word="a123bc34d8ef34"))
print(sol.numDifferentIntegers(word="leet1234code234"))
print(sol.numDifferentIntegers(word="a1b01c001"))

# Problem - https://leetcode.com/problems/number-of-different-integers-in-a-string/description/
