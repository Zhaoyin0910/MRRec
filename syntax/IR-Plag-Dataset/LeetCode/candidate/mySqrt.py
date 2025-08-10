class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        low, high, res = 1, x, -1

        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res