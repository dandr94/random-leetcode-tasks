from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a, b = set(), set()
        C = []
        c = 0

        for i in range(len(A)):
            a.add(A[i])
            b.add(B[i])

            if A[i] == B[i]:
                c += 1
                C.append(c)
                continue

            if A[i] in b:
                c += 1

            if B[i] in a:
                c += 1

            C.append(c)

        return C


sol = Solution()
print(sol.findThePrefixCommonArray(A=[1, 3, 2, 4], B=[3, 1, 2, 4]))
print(sol.findThePrefixCommonArray(A=[2, 3, 1], B=[3, 1, 2]))

# Problem - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
