class Solution:
    def firstUniqChar(self, s: str) -> int:
        l=list(s)
        d=dict()
        c=None
        for i in l:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for key in d.keys():
            if d[key]==1:
                c=key
                break
        if c is None:
            return -1
        for j in range(0,len(l)):
            if c==l[j]:
                return j