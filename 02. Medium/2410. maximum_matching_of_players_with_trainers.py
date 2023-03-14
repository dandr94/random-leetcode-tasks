from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        i = len(players) - 1
        j = len(trainers) - 1

        res = 0

        while i > -1 and j > -1:
            if players[i] <= trainers[j]:
                res += 1
                j -= 1
                i -= 1
                continue

            i -= 1

        return res


sol = Solution()
print(sol.matchPlayersAndTrainers(players=[4, 7, 9], trainers=[8, 2, 5, 8]))
print(sol.matchPlayersAndTrainers(players=[1, 1, 1], trainers=[10]))

# Problem - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
