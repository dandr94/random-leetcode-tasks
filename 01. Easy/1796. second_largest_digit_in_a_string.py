import heapq


class Solution:
    def secondHighest(self, s: str) -> int:
        _set = set()

        for l in s:
            if l.isnumeric():
                _set.add(l)

        _list = list(_set)
        res = heapq.nlargest(2, _list)[-1] if len(_list) > 1 else -1

        return int(res)


sol = Solution()
print(sol.secondHighest(s="dfa12321afd"))
print(sol.secondHighest(s="abc1111"))
print(sol.secondHighest(s="dfa12321afd"))
print(sol.secondHighest(s="ck077"))

# Problem - https://leetcode.com/problems/second-largest-digit-in-a-string/
