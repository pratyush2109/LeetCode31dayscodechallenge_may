class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn=list(ransomNote)
        m=list(magazine)
        d1=dict()
        d2=dict()
        for i in rn:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for j in m:
            if j not in d2:
                d2[j]=1
            else:
                d2[j]+=1
        for key in d1.keys():
            if key not in d2:
                return False
            else:
                if d2[key]<d1[key]:
                    return False
        
        return True