import bisect
from typing import List
import heapq


class KthLargest:
    # def __init__(self, k, nums):
    #     self.k = k
    #     self.heap = []
    #     for num in nums:
    #         heapq.heappush(self.heap, num)
    #         if len(self.heap) > k:
    #             heapq.heappop(self.heap)
    #
    # def add(self, val):
    #     heapq.heappush(self.heap, val)
    #     if len(self.heap) > self.k:
    #         heapq.heappop(self.heap)
    #     return self.heap[0]

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)

        return self.nums[-self.k]


obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))

# Problem - https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
