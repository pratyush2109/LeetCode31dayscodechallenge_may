class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1=dict()
        
        if len(s1)>len(s2):
            return False
        
        l=len(s1)
        for i in s1:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
                
        for i in range(0,len(s2)-len(s1)+1):
            temp=s2[i:i+l]
            if sorted(temp)==sorted(s1):
                return True
            
        return False