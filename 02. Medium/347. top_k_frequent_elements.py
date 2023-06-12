from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums).most_common()

        return [counter[x][0] for x in range(k)]


sol = Solution()
print(sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(sol.topKFrequent(nums=[1], k=1))

# Problem - https://leetcode.com/problems/top-k-frequent-elements/description/
