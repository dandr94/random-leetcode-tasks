class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        if mainTank < 5:
            return mainTank * 10

        i = 0
        while mainTank > 0:
            i += 1

            if i % 5 == 0 and additionalTank:
                mainTank += 1
                additionalTank -= 1

            mainTank -= 1

        return i * 10


sol = Solution()
print(sol.distanceTraveled(mainTank=5, additionalTank=10))
print(sol.distanceTraveled(mainTank=1, additionalTank=2))

# Problem - https://leetcode.com/problems/total-distance-traveled/description/
