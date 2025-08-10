class Solution:
    def isHappy(self, n: int) -> bool:
        a=[]
        s=0
        while(True):
            for i in str(n):
                s+=int(i)**2
            n=s
            s=0
            if(n==1):
                return 1
            if n in a:
                return 0
            a.append(n)