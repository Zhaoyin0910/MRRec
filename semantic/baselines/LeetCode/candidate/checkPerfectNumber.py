from math import sqrt


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return 0

        def is_prime(n):
            if n == 1:
                return 0
            for i in range(2, n):
                if n % i == 0:
                    return 0
            return 1

        if is_prime(num):
            return 0
        L = [1]
        x = 2
        while True:
            if num % x == 0:
                L.extend([x, num // x])
            x += 1
            if x == int(sqrt(num)) + 1:
                break
        return sum(L) == num
