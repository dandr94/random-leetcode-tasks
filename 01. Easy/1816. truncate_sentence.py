class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split(maxsplit=k)[:k])


sol = Solution()
print(sol.truncateSentence(s="Hello how are you Contestant", k=4))
print(sol.truncateSentence(s="What is the solution to this problem", k=4))
print(sol.truncateSentence(s="chopper is not a tanuki", k=5))

# Problem - https://leetcode.com/problems/truncate-sentence/description/
