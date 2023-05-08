from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_amount = Counter(s1)
        left_idx = 0

        for right_idx, char in enumerate(s2):
            char_amount[char] -= 1

            while char_amount[char] < 0:
                char_amount[s2[left_idx]] += 1
                left_idx += 1

            if right_idx - left_idx + 1 == len(s1):
                return True

        return False


sol = Solution()
print(sol.checkInclusion(s1="ab", s2="eidbaooo"))
print(sol.checkInclusion(s1="ab", s2="eidboaoo"))

# Problem - https://leetcode.com/problems/permutation-in-string/
