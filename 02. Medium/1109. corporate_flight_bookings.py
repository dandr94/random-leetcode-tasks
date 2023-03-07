from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1)

        for first, last, seats in bookings:
            res[first - 1] += seats
            res[last] -= seats

        for i in range(1, n):
            res[i] += res[i - 1]

        return res[:-1]


sol = Solution()
print(sol.corpFlightBookings(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))
print(sol.corpFlightBookings(bookings=[[1, 2, 10], [2, 2, 15]], n=2))

# Problem - https://leetcode.com/problems/corporate-flight-bookings/description/
# Cumulative
