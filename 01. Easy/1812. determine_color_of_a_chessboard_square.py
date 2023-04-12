class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        even = '2468'
        odd = '1357'

        if coordinates[0] in 'aceg':
            return coordinates[1] in even
        else:
            return coordinates[1] in odd


sol = Solution()
print(sol.squareIsWhite(coordinates="a1"))
print(sol.squareIsWhite(coordinates="h3"))
print(sol.squareIsWhite(coordinates="c7"))

# Problem - https://leetcode.com/problems/determine-color-of-a-chessboard-square/
