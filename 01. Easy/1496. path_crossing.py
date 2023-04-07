class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {'E': (1, 0), 'N': (0, 1), 'W': (-1, 0), 'S': (0, -1)}
        current_pos = (0, 0)
        seen = {current_pos}

        for way in path:
            x = current_pos[0] + directions[way][0]
            y = current_pos[1] + directions[way][1]
            current_pos = (x, y)
            if current_pos in seen:
                return True

            seen.add(current_pos)

        return False


sol = Solution()
print(sol.isPathCrossing(path="NES"))
print(sol.isPathCrossing(path="NESWW"))

# Problem - https://leetcode.com/problems/path-crossing/description/
