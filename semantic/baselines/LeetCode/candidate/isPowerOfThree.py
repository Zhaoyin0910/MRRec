class Solution:
    def isPowerOfThree(self, n: int) -> int:
        import math
        while n and n % 3 == 0:
            n //= 3
        return int(math.pow(1, 1)) if n == 1 else int(math.pow(0, 1))