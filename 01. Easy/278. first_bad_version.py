# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return n

        start, end = 0, n

        while end - start > 1:
            mid = start + (end - start) // 2

            if isBadVersion(mid):
                end = mid
            else:
                start = mid

        return end



sol = Solution()
print(sol.firstBadVersion(n=5))
print(sol.firstBadVersion(1))

# Problem - https://leetcode.com/problems/first-bad-version/description/