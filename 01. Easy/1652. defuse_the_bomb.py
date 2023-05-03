from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k < 0:
            return self.decrypt(code[::-1], -k)[::-1]

        _len = len(code)
        res = [0] * _len
        _sum = sum(code[:k])
        for idx, num in enumerate(code):
            _sum += code[(idx + k) % _len] - num
            res[idx] = _sum

        return res



sol = Solution()
print(sol.decrypt(code=[5, 7, 1, 4], k=3))
print(sol.decrypt(code=[1, 2, 3, 4], k=0))
print(sol.decrypt(code=[2, 4, 9, 3], k=-2))

# Problem - https://leetcode.com/problems/defuse-the-bomb/description/