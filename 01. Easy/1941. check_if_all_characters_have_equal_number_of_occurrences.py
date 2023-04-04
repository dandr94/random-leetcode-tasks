class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}

        for l in s:
            if l not in d:
                d[l] = 1
            else:
                d[l] += 1

        res = set(d.values())

        return len(res) == 1


sol = Solution()
print(sol.areOccurrencesEqual(s="abacbc"))
print(sol.areOccurrencesEqual(s="aaabb"))

# Problem - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/
