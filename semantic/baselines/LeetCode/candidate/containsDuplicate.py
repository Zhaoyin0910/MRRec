class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet=set(nums)
        if len(numSet)==len(nums) :
            return 0
        return 1