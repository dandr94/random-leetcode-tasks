from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]
        for i in range(1,n+1):
            counter.append(counter[i>>1] + i%2)
        return counter 


sol = Solution()
print(sol.countBits(n=2))
print(sol.countBits(n=5))