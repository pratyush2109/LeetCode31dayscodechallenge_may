class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q=list()
        flood=list()
        flood.append([sr,sc])
        q.append([sr,sc])
        value=image[sr][sc]
        row_count=len(image[0])
        col_count=len(image)
        while(len(q)!=0):
            ob=q.pop(0)
            r=ob[0]
            c=ob[1]

            if (r-1 in range(0,len(image))) and (c in range(0,len(image[r-1]))):
                if [r-1,c] not in flood:
                    if image[r-1][c]==value:
                        flood.append([r-1,c])
                        q.append([r-1,c])
                        
            if (r in range(0,len(image))) and (c+1 in range(0,len(image[r]))):
                if [r,c+1] not in flood:
                    if image[r][c+1]==value:
                        flood.append([r,c+1])
                        q.append([r,c+1])
                
            if (r+1 in range(0,len(image))) and (c in range(0,len(image[r+1]))):
                if [r+1,c] not in flood:
                    if image[r+1][c]==value:
                        flood.append([r+1,c])
                        q.append([r+1,c])
                
            if (r in range(0,len(image))) and (c-1 in range(0,len(image[r]))):
                if [r,c-1] not in flood:
                    if image[r][c-1]==value:
                        flood.append([r,c-1])
                        q.append([r,c-1])
                      
    
        for i in flood:
            r=i[0]
            c=i[1]
            image[r][c]=newColor
        
        return image