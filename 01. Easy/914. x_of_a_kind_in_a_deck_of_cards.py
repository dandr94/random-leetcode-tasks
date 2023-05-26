from typing import List
import collections
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return math.gcd(*collections.Counter(deck).values()) != 1

sol = Solution()
print(sol.hasGroupsSizeX(deck = [1,2,3,4,4,3,2,1]))
print(sol.hasGroupsSizeX(deck = [1,1,1,2,2,2,3,3]))

# Problem - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/