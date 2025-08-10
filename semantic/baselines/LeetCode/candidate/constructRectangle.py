class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        拿到题其实没思路:
            条件1: L >= W
            条件2: L 和 W差距尽量小
            条件3: L * W == area

            根据条件1和条件3分析可知 W <= area * 0.5
            根据条件2可知 W 需要尽量靠近area * 0.5, 也就是需要遍历
        """
        wide, height = 1, area  # 起始必定有1 * area = area
        limit = int(area ** 0.5)
        for i in range(2, limit + 1):
            new_h = area // i
            if new_h * i == area:  # 因为new_h是取整得到的, 所有可能不相等
                wide, height = i, new_h
        return [height, wide]


s1 = Solution()
m = 2
root = s1.constructRectangle(m)
print(root)