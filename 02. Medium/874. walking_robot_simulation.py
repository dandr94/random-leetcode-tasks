from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = y = best = dx = 0
        dy = 1
        obstacles_set = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -2:
                dx, dy = -dy, dx
            elif cmd == -1:
                dx, dy = dy, -dx
            elif 1 <= cmd <= 9:
                for i in range(cmd):
                    if (x + dx, y + dy) in obstacles_set:
                        break
                    else:
                        x += dx
                        y += dy

                best = max(best, x * x + y * y)
        return best


sol = Solution()
print(sol.robotSim([4, -1, 3], []))
print(sol.robotSim([4, -1, 4, -2, 4], [[2, 4]]))
print(sol.robotSim([6, -1, -1, 6], []))

# Problem - https://leetcode.com/problems/walking-robot-simulation/
