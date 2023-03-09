class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False

        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                return False

        return True

        # return len(set(zip(s,t))) == len(set(s)) == len(set(t))


sol = Solution()
print(sol.isIsomorphic(s="egg", t="add"))
print(sol.isIsomorphic(s="foo", t="bar"))
print(sol.isIsomorphic(s="paper", t="title"))

# Problem - https://leetcode.com/problems/isomorphic-strings/description/
