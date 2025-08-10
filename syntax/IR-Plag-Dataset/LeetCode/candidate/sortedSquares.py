class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 找到离原点最近的也就是绝对值最小的那个数及其下标
        idx = 0
        val = 1e4
        for i in range(len(nums)):
            if abs(nums[i]) < val:
                val = abs(nums[i])
                idx = i

        # 从idx开始中心扩散
        res = [nums[idx] ** 2]
        i, j = idx - 1, idx + 1
        while i >= 0 and j < len(nums):
            if abs(nums[i]) < abs(nums[j]):
                res.append(nums[i] ** 2)
                i -= 1
            else:
                res.append(nums[j] ** 2)
                j += 1

        # 当有一个指针到头时要判断处理另一个指针
        while i >= 0:
            res.append(nums[i] ** 2)
            i -= 1
        while j < len(nums):
            res.append(nums[j] ** 2)
            j += 1

        return res
