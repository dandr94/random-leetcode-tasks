from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        eliminated = 0
        temp = [d / s for d, s in zip(dist, speed)]
        temp.sort()

        while eliminated < len(temp):
            if temp[eliminated] > eliminated:
                eliminated += 1
            else:
                break

        return eliminated


sol = Solution()
print(sol.eliminateMaximum(dist=[1, 3, 4], speed=[1, 1, 1]))
print(sol.eliminateMaximum(dist=[1, 1, 2, 3], speed=[1, 1, 1, 1]))
print(sol.eliminateMaximum(dist=[3, 2, 4], speed=[5, 3, 2]))

# Problem - https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/
