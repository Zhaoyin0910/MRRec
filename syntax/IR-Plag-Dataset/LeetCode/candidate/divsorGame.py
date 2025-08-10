class Solution:
    def divisorGame(self, N: int) -> bool:
        # 枚举在n之前的每一种情况
        ret = [0]*(N+1)
        if N<=1:return 0
        #当N是1的时候，爱丽丝先拿，但是他拿不了，所以他肯定输了
        ret[1] = 0
        #当N是2的时候，爱丽丝只能拿1，N剩下1；bob没办法拿，所以爱丽丝肯定是赢了
        ret[2] = 1
        #等于1和2的情况都满足了接下来根据前面两种情况递推后面的情况
        if N >= 3:
            for i in range(3,N+1):
                #N % x == 0表明x一定是N的约数，所以最大的情况就是当
                                                #N为偶数，偶数的一半
                                                #N为奇数，奇数的一半向下取整
                for j in range(1,i//2):
                #假如N为三，爱丽丝可拿的数就是j=1，剩下i-j=2，ret[2]是1，又回到了爱丽丝拿1,必输的情况
                    if i%j==0 and ret[i-j]==0:
                        ret[i]=1
                        break

        return ret[N]==1