class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        c = 0

        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            c += 1

        return c


sol = Solution()
print(sol.countOperations(num1=2, num2=3))
print(sol.countOperations(num1=10, num2=10))

# Problem - https://leetcode.com/problems/count-operations-to-obtain-zero/description/
