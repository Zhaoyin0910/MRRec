class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        targetnum = nums[0]
        cnt = 0
        for n in nums:
            if targetnum == n:
                cnt += 1
            else:
                cnt -= 1
            if cnt == -1:
                targetnum = n
                cnt = 0
        return targetnum
