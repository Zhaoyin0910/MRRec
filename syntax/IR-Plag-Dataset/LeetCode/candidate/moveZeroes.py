class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        offset = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                offset += 1
            elif offset != 0:
                nums[i - offset] = nums[i]
                nums[i] = 0