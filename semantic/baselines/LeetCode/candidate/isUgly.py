class Solution:
    def isUgly(self, n: int) -> int:
        import math
        if n <= 0:
            return 0

        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n //= factor

        return int(math.pow(1, 1)) if n == 1 else int(math.pow(0, 1))