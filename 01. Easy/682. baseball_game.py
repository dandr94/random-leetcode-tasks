from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []

        for operation in operations:
            if operation == '+':
                if len(records) > 1:
                    records.append(records[-1] + records[-2])
            elif operation == 'D':
                if records:
                    records.append(records[-1] * 2)
            elif operation == 'C':
                if records:
                    records.pop()
            else:
                records.append(int(operation))

        return sum(records)


sol = Solution()
print(sol.calPoints(operations=["5", "2", "C", "D", "+"]))
print(sol.calPoints(operations=["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(sol.calPoints(operations=["1", "C"]))

# Problem - https://leetcode.com/problems/baseball-game/description/
