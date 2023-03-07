class Solution:
    def removeDuplicateLetters(self, s):
        last_occ = {l: i for i, l in enumerate(s)}
        stack = []
        visited = set()

        for idx, letter in enumerate(s):
            if letter not in visited:
                while stack and stack[-1] > letter and last_occ[stack[-1]] > idx:
                    visited.remove(stack.pop())

                stack.append(letter)
                visited.add(letter)

        return ''.join(stack)


sol = Solution()
print(sol.removeDuplicateLetters(s="bcabc"))
print(sol.removeDuplicateLetters(s="cbacdcbc"))

# Problem - https://leetcode.com/problems/remove-duplicate-letters/description/
