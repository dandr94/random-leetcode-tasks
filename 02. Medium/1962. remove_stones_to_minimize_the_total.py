import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapq.heapify(piles)

        while k:
            heapq.heapreplace(piles, piles[0] // 2)
            k -= 1
        return -sum(piles)


sol = Solution()
print(sol.minStoneSum(piles=[5, 4, 9], k=2))
print(sol.minStoneSum(piles=[4, 3, 6, 7], k=3))

# Problem - https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/
