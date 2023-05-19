from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0

        for citizen in details:
            _split = list(citizen)
            age = citizen[11:13]
            if int(age) > 60:
                c += 1

        return c


sol = Solution()
print(sol.countSeniors(details=["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
print(sol.countSeniors(details=["1313579440F2036", "2921522980M5644"]))

# Problem - https://leetcode.com/problems/number-of-senior-citizens/description/
