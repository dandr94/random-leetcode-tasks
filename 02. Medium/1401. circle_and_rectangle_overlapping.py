class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        dx = xCenter - max(x1, min(xCenter, x2))
        dy = yCenter - max(y1, min(yCenter, y2))

        return dx * dx + dy * dy <= radius * radius


sol = Solution()
print(sol.checkOverlap(radius=1, xCenter=0, yCenter=0, x1=1, y1=-1, x2=3, y2=1))
print(sol.checkOverlap(radius=1, xCenter=1, yCenter=1, x1=1, y1=-3, x2=2, y2=-1))
print(sol.checkOverlap(radius=1, xCenter=0, yCenter=0, x1=-1, y1=0, x2=0, y2=1))

# Problem - https://leetcode.com/problems/circle-and-rectangle-overlapping/description/
