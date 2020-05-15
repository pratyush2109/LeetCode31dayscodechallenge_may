class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n=len(A)
        max_so_far=0
        max_ending_here=0
        flag=1
        for i in range(n):
            if A[i]>0:
                flag=0
                break
        if flag==1:
            return max(A)
        
        for i in range(n):
            max_ending_here=max_ending_here+A[i]
            if(max_ending_here<0):
                max_ending_here=0
            if max_so_far < max_ending_here:
                max_so_far=max_ending_here
        
        max_kadane=max_so_far
        
        max_wrap=0
        for i in range(n):
            max_wrap+=A[i]
            A[i] = -A[i]

        max_so_far=0
        max_ending_here=0
        n=len(A)
        for i in range(n):
            max_ending_here=max_ending_here+A[i]
            if(max_ending_here<0):
                max_ending_here=0
            if max_so_far < max_ending_here:
                max_so_far=max_ending_here
            
        max_wrap=max_wrap + max_so_far
        
        if max_wrap > max_kadane:
            return max_wrap
        else:
            return max_kadane
        