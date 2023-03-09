from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_1 = {word: idx for idx, word in enumerate(list1)}
        dict_2 = {word: dict_1[word] + idx for idx, word in enumerate(list2) if word in dict_1}

        dict_2 = sorted(dict_2.items(), key=lambda x: x[1])

        lowest = dict_2[0][1]
        res = [dict_2[0][0]]
        for k, v in dict_2[1:]:
            if v > lowest:
                break

            res.append(k)

        return res


sol = Solution()
print(sol.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
                         list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
print(sol.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
                         list2=["KFC", "Shogun", "Burger King"]))
print(sol.findRestaurant(list1=["happy", "sad", "good"], list2=["sad", "happy", "good"]))

# Problem - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
