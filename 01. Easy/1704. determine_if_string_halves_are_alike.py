class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        mid = len(s) // 2
        prefix = s[:mid]
        suffix = s[mid:]
        c1 = [x for x in prefix if x in vowels]
        c2 = [x for x in suffix if x in vowels]

        return len(c1) == len(c2)


sol = Solution()
print(sol.halvesAreAlike(s="book"))
print(sol.halvesAreAlike(s="textbook"))

# Problem - https://leetcode.com/problems/determine-if-string-halves-are-alike/
