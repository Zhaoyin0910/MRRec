class Solution:
def plusOne(self, digits: List[int]) -> List[int]:
        newstr = ''
        n = len(digits)
        # list -> str
        for i in digits:
            newstr += str(i)
        # str -> int
        newnum = int(newstr)
        newnum += 1
        # int -> str
        newnewstr = str(newnum)
        newnewstr = newnewstr.zfill(n)
        newlst = []
        # str -> list
        for i in newnewstr:
            newlst.append(int(i))
        return newlst