class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: return 0
        while n>1:
            if n%2 == 0:
                n //= 2
            else:
                return 0
        return 1