class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        total = 0
        res = 0
        curSum = 0
        for i in range(n):
            total += nums[i]
        curSum = n * (n + 1) // 2
        res = curSum - total
        return res