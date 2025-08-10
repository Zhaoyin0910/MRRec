def two_sum(nums: List[int], target: int) -> List[int]:
    size = len(nums)
    for i, m in enumerate(nums):
        j = i + 1
        while j < size:
            if target == (m + nums[j]):
                return [i, j]
            else:
                # print(i, j, m + _n, " didn't match!")
                j += 1