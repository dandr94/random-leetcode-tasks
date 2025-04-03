class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in unique_chars and unique_chars[char] >= left:
                left = unique_chars[char] + 1

            unique_chars[char] = right

            max_len = max(max_len, right - left + 1)

        return max_len


sol = Solution()
print(sol.lengthOfLongestSubstring(s="abcabcbb"))
print(sol.lengthOfLongestSubstring(s="bbbbb"))
print(sol.lengthOfLongestSubstring(s="pwwkew"))
print(sol.lengthOfLongestSubstring(s="aab"))

# Medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
