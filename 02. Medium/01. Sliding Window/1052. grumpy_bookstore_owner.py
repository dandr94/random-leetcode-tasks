from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        best_window_sum = 0
        window_sum = 0
        not_grumpy_sum = 0

        for right in range(len(customers)):
            if grumpy[right] == 0:
                not_grumpy_sum += customers[right]
            else:
                window_sum += customers[right]

            if right - left + 1 > minutes:
                if grumpy[left] == 1:
                    window_sum -= customers[left]

                left += 1

            best_window_sum = max(best_window_sum, window_sum)

        return best_window_sum + not_grumpy_sum


sol = Solution()
print(sol.maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5],
                       grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3))
print(sol.maxSatisfied(customers=[1], grumpy=[0], minutes=1))

# Medium
# https://leetcode.com/problems/grumpy-bookstore-owner/description/
