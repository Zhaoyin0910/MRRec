class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #长度小于3的，直接返回最大值
        ll_nums = list(set(nums))
        if len(ll_nums) < 3:
            return max(ll_nums)
        #初始化最大值，次大值，第三大值
        a = b = c = float('-inf')
        #遍历列表：
        for num in nums:
            #大于最大值，依次更新，这里要注意更新顺序，先更新c, 然后b, 最后a
            if num > a:
                c = b
                b = a
                a = num
            #更新次大值
            elif num > b and num != a:
                c = b
                b = num
            #更新第三大值
            elif num > c and num != a and num != b:
                c = num
        return c