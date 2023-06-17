from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [s]
        for idx, char in enumerate(s):
            if char.isalpha():
                for j in range(len(res)):
                    comb = list(res[j])
                    comb[idx] = comb[idx].swapcase()
                    res.append(''.join(comb))
        return res


sol = Solution()
print(sol.letterCasePermutation(s="a1b2"))
print(sol.letterCasePermutation(s="3z4"))

# Problem - https://leetcode.com/problems/letter-case-permutation/description/
