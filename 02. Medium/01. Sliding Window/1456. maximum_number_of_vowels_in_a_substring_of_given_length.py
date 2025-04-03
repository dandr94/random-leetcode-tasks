class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = sum(1 for char in s[:k] if char in vowels)
        max_count = count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1

            if s[i] in vowels:
                count += 1

            max_count = max(max_count, count)

        return max_count


sol = Solution()
print(sol.maxVowels(s="abciiidef", k=3))
print(sol.maxVowels(s="aeiou", k=2))
print(sol.maxVowels(s="leetcode", k=3))

# Medium
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
