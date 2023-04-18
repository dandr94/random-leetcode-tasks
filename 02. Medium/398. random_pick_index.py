from typing import List
from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = randint(1, count)
                if chance == count:
                    res = i
        return res

    # def __init__(self, nums: List[int]):
    #     self.dict_nums = defaultdict(list)
    #     for idx, n in enumerate(nums):
    #         self.dict_nums[n].append(idx)
    #
    # def pick(self, target: int) -> int:
    #     _choice = choice(self.dict_nums[target])
    #     return _choice


sol = Solution(nums=[1, 2, 3, 3, 3])
sol.pick(3)
sol.pick(1)
sol.pick(3)

# Problem - https://leetcode.com/problems/random-pick-index/
