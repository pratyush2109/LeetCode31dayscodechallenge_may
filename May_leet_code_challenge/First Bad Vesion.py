# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        mid=(low+high)//2
        while(True):
            if(isBadVersion(mid)):
                if(not(isBadVersion(mid-1))):
                    return mid
                else:
                    high=mid
                    mid=(low+high)//2
            else:
                if(isBadVersion(mid+1)):
                    return (mid+1)
                else:
                    low=mid
                    mid=(low+high)//2
        