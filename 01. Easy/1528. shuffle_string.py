from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0] * len(s)

        for idx, i in enumerate(indices):
            res[i] = s[idx]

        return ''.join(res)


sol = Solution()
print(sol.restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))
print(sol.restoreString(s="abc", indices=[0, 1, 2]))

# Problem - https://leetcode.com/problems/shuffle-string/description/
