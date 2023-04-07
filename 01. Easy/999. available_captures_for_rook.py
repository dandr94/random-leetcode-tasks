import pprint
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        directions_dict = {
            1: lambda r, c: (r, c - 1),
            2: lambda r, c: (r, c + 1),
            3: lambda r, c: (r - 1, c),
            4: lambda r, c: (r + 1, c),
        }

        def is_valid_position(board, r, c):
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                return True
            return False

        rook_row = 0
        rook_col = 0

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'R':
                    rook_row = row
                    rook_col = col
                    break

        pawns_captured = 0

        for i in range(1, len(directions_dict) + 1):
            current_row = rook_row
            current_col = rook_col
            while True:
                step = directions_dict[i]
                next_row, next_col = step(current_row, current_col)
                if is_valid_position(board, next_row, next_col):
                    if board[next_row][next_col] == 'p':
                        pawns_captured += 1
                        break
                    elif board[next_row][next_col] == 'B':
                        break
                    current_row, current_col = next_row, next_col
                else:
                    break
        return pawns_captured


sol = Solution()
print(sol.numRookCaptures(board=[[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                                 [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
                                 [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                                 [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
print(sol.numRookCaptures(board=[[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                                 [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
                                 [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                                 [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
print(sol.numRookCaptures(board=[[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                                 [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
                                 [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
                                 [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))

# Problem - https://leetcode.com/problems/available-captures-for-rook/description/
