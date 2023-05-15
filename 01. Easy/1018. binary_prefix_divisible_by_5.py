from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """
        :return:  A new list of booleans of the same length as `nums`. The i-th element of the returned list
                    is True if and only if the prefix of `nums` from index 0 up to and including i is divisible by 5.
        """

        res = []
        holder = 0

        for bit in nums:
            # We can compute the remainder after dividing by 5 of a binary number by first multiplying the
            # previous remainder by 2 and then adding the next bit, and finally taking the remainder after
            # dividing by 5. This is because 2^k % 5 = 2^(k % 4) % 5 for any non-negative integer k.
            holder = (holder * 2 + bit) % 5
            # If the remainder is 0, then the prefix from index 0 up to and including i is divisible by 5.
            res.append(holder == 0)

        return res


sol = Solution()
print(sol.prefixesDivBy5(nums=[0, 1, 1]))
print(sol.prefixesDivBy5(nums=[1, 1, 1]))

# Problem - https://leetcode.com/problems/binary-prefix-divisible-by-5/
