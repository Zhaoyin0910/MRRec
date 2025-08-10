
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)
        ch = '0'
        for i in range(2,len(b)-1):
            ch = b[i]
            if ch != b[i+1]:
                ch = b[i+1]
            else:
                return 0
        return 1