class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n=len(coordinates)
        xc=1
        yc=1
        xi=coordinates[0][0]
        yi=coordinates[0][1]
        slope=list()
        
        for i in range(1,n):
            if xi==coordinates[i][0]:
                xc+=1
            if yi==coordinates[i][1]:
                yc+=1
        
        if xc==n or yc==n:
            return True
        
        for i in range(0,n-1):
            x=coordinates[i+1][0]-coordinates[i][0]
            y=coordinates[i+1][1]-coordinates[i][1]
            if x!=0:
                m=y/x
                slope.append(m)
            else:
                slope.append(99999)
        
        unique_slope=set(slope)
        unique=list(unique_slope)
        
        if len(unique)==1:
            return True
        else:
            return False