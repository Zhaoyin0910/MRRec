class Solution:
    def hammingWeight(self, n: int) -> int:
        ns = str(bin(n))
        cnt = 0

        for i in ns:
            if i == "1":
                cnt += 1

        return cnt