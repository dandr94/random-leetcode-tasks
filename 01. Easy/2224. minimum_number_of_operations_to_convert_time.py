class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curr = 60 * int(current[0:2]) + int(current[3:5])
        corr = 60 * int(correct[0:2]) + int(correct[3:5])
        diff = corr - curr
        count = 0
        for m in [60, 15, 5, 1]:
            count += diff // m
            diff %= m
        return count


sol = Solution()
print(sol.convertTime(current="02:30", correct="04:35"))
print(sol.convertTime(current="11:00", correct="11:01"))

# Problem - https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/description/
