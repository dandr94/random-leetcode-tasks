from typing import List


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        from functools import lru_cache

        @lru_cache()
        def dp(i, j):
            if j - i == 1:
                return {int(s[i])}
            possible = set()
            for idx in range(i + 1, j, 2):
                for a in dp(i, idx):
                    for b in dp(idx + 1, j):
                        val = a * b if s[idx] == '*' else a + b
                        if val <= 1000:
                            possible.add(val)
            return possible

        correct = eval(s)
        answers = filter(lambda ans: ans in dp(0, len(s)), answers)
        return sum([5 if ans == correct else 2 for ans in answers])


sol = Solution()
print(sol.scoreOfStudents(s="7+3*1*2", answers=[20, 13, 42]))
print(sol.scoreOfStudents(s="3+5*2", answers=[13, 0, 10, 13, 13, 16, 16]))
print(sol.scoreOfStudents(s="6+0*1", answers=[12, 9, 6, 4, 8, 6]))

# Problem - https://leetcode.com/problems/the-score-of-students-solving-math-expression/description/