class Solution:
    def punishmentNumber(self, n: int) -> int:
        # pos = {
        #     1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379,
        #     414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000};
        #
        # return sum(i * i for i in pos if i <= n)

        def is_possible_partition(s, sum_left, idx):
            if sum_left == 0 and idx == len(s):
                return True

            for i in range(idx, len(s)):
                num = int(s[idx: i + 1])

                if num > sum_left:
                    break
                if is_possible_partition(s, sum_left - num, i + 1):
                    return True

            return False

        res = 0

        for i in range(1, n + 1):
            if is_possible_partition(str(i * i), i, 0):
                res += i * i

        return res


sol = Solution()
print(sol.punishmentNumber(n=10))
print(sol.punishmentNumber(n=37))

# Problem - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/
