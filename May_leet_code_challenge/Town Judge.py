class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted_by=dict() # here trusted by means i is trusted upon by 
        for i in range(1,N+1):
            l=list()
            for j in trust:
                if j[1]==i:
                    l.append(j[0])
            trusted_by[i]=l
        
        t=list()
        for i in trust:
            if i[0] not in t:
                t.append(i[0])
        
        
        for i in trusted_by:
            if i not in t:
                if len(trusted_by[i])==N-1:
                    return i
        
        return -1