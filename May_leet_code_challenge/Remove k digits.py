class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res=list()
        count=k
        
        for i in num:
            while count and res and res[-1] > i:
                res.pop()
                count-=1
            res.append(i)
        n="".join(res[0:len(num)-k]).lstrip("0")
        if len(n):
            return n
        else:
            return "0"