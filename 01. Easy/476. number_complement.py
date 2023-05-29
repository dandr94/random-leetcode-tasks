class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        comp = ''

        for i in binary:
            comp += '1' if i == '0' else '0'
            
        return int(comp, 2)


sol = Solution()
print(sol.findComplement(num=5))
print(sol.findComplement(num=1))


# Problem - https://leetcode.com/problems/number-complement/description/