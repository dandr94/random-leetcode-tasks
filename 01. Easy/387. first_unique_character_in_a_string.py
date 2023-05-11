class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()
        for idx, char in enumerate(s):
            if char not in s[idx + 1:] and char not in visited:
                return idx
            visited.add(char)
        return - 1


sol = Solution()
print(sol.firstUniqChar(s="leetcode"))
print(sol.firstUniqChar(s="loveleetcode"))
print(sol.firstUniqChar(s="aabb"))

# Problem - https://leetcode.com/problems/first-unique-character-in-a-string/description/
