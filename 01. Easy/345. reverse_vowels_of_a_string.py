class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        s_list = list(s)
        s_vowels = [x for x in s_list if x in vowels]

        for i in range(len(s)):
            if s[i] not in vowels:
                s_list[i] = s[i]
            else:
                s_list[i] = s_vowels.pop()


        return "".join(s_list)


sol = Solution()
print(sol.reverseVowels(s = "hello"))
print(sol.reverseVowels(s = "leetcode"))

# Problem - https://leetcode.com/problems/reverse-vowels-of-a-string/