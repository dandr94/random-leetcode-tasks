class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        pow_4 = 10 ** 4

        bulky = length >= pow_4 or width >= pow_4 or height >= pow_4 or length * width * height >= 10 ** 9
        heavy = mass >= 100

        if bulky and heavy:
            return 'Both'
        elif bulky and not heavy:
            return 'Bulky'
        elif not bulky and heavy:
            return 'Heavy'
        else:
            return 'Neither'


sol = Solution()
print(sol.categorizeBox(length=1000, width=35, height=700, mass=300))
print(sol.categorizeBox(length=200, width=50, height=800, mass=50))

# Problem - https://leetcode.com/problems/categorize-box-according-to-criteria/description/
