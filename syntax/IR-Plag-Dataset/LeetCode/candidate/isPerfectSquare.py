class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            res = mid * mid
            if res == num and isinstance(res, int):
                return True
            elif res < num:
                left = mid + 1
            else:
                right = mid - 1

        return 0