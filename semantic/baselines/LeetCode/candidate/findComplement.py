class Solution:
    def findComplement(self, num: int) -> int:
        list_two_num = list(bin(num).replace('0b',''))
        for i in range(len(list_two_num)):
            if list_two_num[i] == '0':
                list_two_num[i] = '1'
            else:
                list_two_num[i] = '0'
        res = ''.join(list_two_num)
        return(int(res,2))