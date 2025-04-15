from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0

        while i < len(flowerbed) and n:
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    n -= 1
                    flowerbed[i] = 1
                    i += 1  # skip the next plot, since it can't be used
            i += 1

        return n == 0


sol = Solution()
print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))

# Easy
# https://leetcode.com/problems/can-place-flowers/description/
