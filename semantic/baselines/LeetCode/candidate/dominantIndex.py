class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max = 0
        subMax = 0
        if len(nums) < 2:
            return 0
        if nums[0] > nums[1]:
            max = 0
            subMax = 1
        else:
            max = 1
            subMax = 0
        for i in range(2, len(nums)):
            if nums[i] > nums[max]:
                subMax = max
                max = i
            else:
                if nums[i] > nums[subMax]:
                    subMax = i
        if nums[max] >= nums[subMax] * 2:
            return max
        else:
            return -1
