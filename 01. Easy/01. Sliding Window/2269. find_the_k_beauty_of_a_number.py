class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        _string = str(num)
        answer = 0

        for i in range(len(_string) - k + 1):
            substring = _string[i:i + k]

            if int(substring) == 0:
                continue

            if num % int(substring) == 0:
                answer += 1

        return answer


sol = Solution()
print(sol.divisorSubstrings(num=240, k=2))
print(sol.divisorSubstrings(num=430043, k=2))

# Easy
# https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/
