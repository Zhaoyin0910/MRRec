class Solution:
    def toHex(self, num: int) -> str:
#编制16进制字典
#如果num>0，每次把num%16的结果加入ans的前边，用num//16的结果替代num，直到num为0
#如果num=0，直接返回'0'
#如果num<0，进行补码运算，补码运算其实就是用计算位数允许的最大值作为上限，超过它就进行模运算，而负数的补码运算相当于用最大值
#4294967296加上num，再进行正常的16进制转换即可
        dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8:'8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        ans = ''
        if num > 0:
            while num != 0:
                ans = dic[num % 16] + ans
                num = num // 16
            return ans
        elif num == 0:
            return "0"
        else:
            num = 4294967296 + num
            while num != 0:
                ans = dic[num % 16] + ans
                num = num // 16
            return ans