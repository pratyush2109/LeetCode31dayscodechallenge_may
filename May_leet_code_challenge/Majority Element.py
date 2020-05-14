class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=dict()
        n=(len(nums))//2
        unique_set=set(nums)
        unique=list(unique_set)
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in unique:
            if d[i]>n:
                return i