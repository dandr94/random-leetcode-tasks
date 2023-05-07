class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24


sol = Solution()
print(sol.findDelayedArrivalTime(arrivalTime=15, delayedTime=5))
print(sol.findDelayedArrivalTime(arrivalTime=13, delayedTime=11))

# Problem - https://leetcode.com/problems/calculate-delayed-arrival-time/
