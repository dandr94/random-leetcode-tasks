from collections import Counter, defaultdict
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [num for num, _ in Counter(nums).most_common(k)]

        # seen = defaultdict(int)
        # for num in nums:
        #     seen[num] += 1
        #
        # sort = sorted(seen.items(), key=lambda x: -x[1])
        # res = [sort[i][0] for i in range(k)]
        # return res

        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1

        heap = []
        for num, count in seen.items():
            heapq.heappush(heap, (-count, num))

        res = [heapq.heappop(heap)[1] for _ in range(k)]

        return res


sol = Solution()
print(sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(sol.topKFrequent(nums=[1], k=1))

# Medium
# https://leetcode.com/problems/top-k-frequent-elements/
