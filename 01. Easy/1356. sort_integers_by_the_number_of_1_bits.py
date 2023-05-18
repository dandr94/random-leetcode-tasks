import heapq
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """
        :return: - A new list containing the integers from `arr`, sorted in ascending order based on the number of
                     1 bit in their binary representation.
        """
        # return sorted(arr, key=lambda x: [bin(x).count('1'), x])

        temp = []
        res = []

        def count_1s(num):
            c = 0

            while num:
                num &= num - 1
                c += 1
            return c

        # Push (count_1s(n), n) tuples into the heap for each n in arr
        for n in arr:
            heapq.heappush(temp, (count_1s(n), n))

        # Pop elements from the heap and append the second element of the tuple (n) to the result list
        while temp:
            res.append(heapq.heappop(temp)[1])

        return res


sol = Solution()
print(sol.sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(sol.sortByBits(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))

# Problem - https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
