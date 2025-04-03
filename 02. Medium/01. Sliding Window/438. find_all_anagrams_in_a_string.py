from typing import List
from collections import deque, Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # size = len(p)
        # left = 0
        # p_count = Counter(p)
        # current_count = Counter(s[:size])
        # answer = []
        #
        # if current_count == p_count:
        #     answer.append(0)
        #
        # for right in range(size, len(s)):
        #     current_count[s[right]] += 1
        #
        #     current_count[s[left]] -= 1
        #     if current_count[s[left]] == 0:
        #         del current_count[s[left]]
        #
        #     if current_count == p_count:
        #         answer.append(left + 1)
        #
        #     left += 1
        #
        # return answer

        char_amount = Counter(p)
        answer = []
        left = 0

        for right, char in enumerate(s):
            char_amount[char] -= 1

            while char_amount[char] < 0:
                char_amount[s[left]] += 1
                left += 1

            if right - left + 1 == len(p):
                answer.append(left)

        return answer


sol = Solution()
print(sol.findAnagrams(s="cbaebabacd", p="abc"))
print(sol.findAnagrams(s="abab", p="ab"))

# Medium
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
