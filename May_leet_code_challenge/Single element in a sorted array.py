class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d=dict()
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d.keys():
            if d[i]==1:
                return i