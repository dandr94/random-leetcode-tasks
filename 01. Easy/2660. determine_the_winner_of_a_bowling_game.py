from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        p1, p2 = 0, 0
        d1, d2 = 0, 0

        for i in range(len(player1)):
            if d1 != 0:
                p1 += player1[i] * 2
                d1 -= 1
            else:
                p1 += player1[i]
            if d2 != 0:
                p2 += player2[i] * 2
                d2 -= 1
            else:
                p2 += player2[i]
            if player1[i] == 10:
                d1 = 2
            if player2[i] == 10:
                d2 = 2

        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2
        else:
            return 0


sol = Solution()
print(sol.isWinner(player1=[4, 10, 7, 9], player2=[6, 5, 2, 3]))
print(sol.isWinner(player1=[3, 5, 7, 6], player2=[8, 10, 10, 2]))
print(sol.isWinner(player1=[2, 3], player2=[4, 1]))

# Problem - https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/
