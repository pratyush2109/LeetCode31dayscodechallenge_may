class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num==1:
            return True
        else:
            i=2
            while(i<=num//2):
                sq=i**2
                if sq==num:
                    return True
                elif sq>num:
                    return False
                else:
                    i+=1