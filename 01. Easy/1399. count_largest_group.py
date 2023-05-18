class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        :return: The number of groups that have the largest sum of digits among numbers from 1 to `n`.
        """
        mapping = {}

        for num in range(1, n + 1):
            _sum = 0
            temp = num

            while temp != 0:
                _sum += temp % 10
                temp //= 10

            mapping[_sum] = mapping.get(_sum, 0) + 1

        _max = max(mapping.values())

        return sum(1 for v in mapping.values() if v == _max)


sol = Solution()
print(sol.countLargestGroup(n=13))
print(sol.countLargestGroup(n=2))

# Problem - https://leetcode.com/problems/count-largest-group/
