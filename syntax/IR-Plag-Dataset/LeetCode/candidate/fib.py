class Solution:
    def fib(self, N: int) -> int:
        if N == 0 : return 0
        if N == 1: return 1
        n1 = 0
        n2 = 1
        n3 = 1
        for i in range(3, N + 1):
            n1 = n2
            n2 = n3
            n3 = n1 + n2
            print(n1, n2, n3)
        return n3