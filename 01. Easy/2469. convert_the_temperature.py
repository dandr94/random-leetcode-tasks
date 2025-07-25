from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32]


sol = Solution()
print(sol.convertTemperature(36.50))
print(sol.convertTemperature(122.11))

# Problem - https://leetcode.com/problems/convert-the-temperature/description/
