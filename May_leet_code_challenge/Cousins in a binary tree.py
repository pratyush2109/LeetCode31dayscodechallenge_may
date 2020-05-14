# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q=[]
        parent=dict()
        level=dict()
        elements=list()
        if x==root.val or y==root.val:
            return False
        q.append(root)
        q.append(1000)
        elements.append(root.val)
        count=101
        l=1
        while len(q)>0:
            temp=q.pop(0)
            if temp==1000:
                if len(q)!=0:
                    if q[0]!=1000:
                        q.append(1000)
                    l+=1
            else:
                if temp is not None:
                    if temp.left is not None:
                        q.append(temp.left)
                        elements.append(temp.left.val)
                        parent[temp.left.val]=temp.val
                        level[temp.left.val]=l
                    elif temp.left is None and temp.right is not None:
                        q.append(temp.left)
                        elements.append(temp.left)
                        parent[count]=temp.val
                        level[count]=l
                        count+=1
                    if temp.right is not None:
                        q.append(temp.right)
                        elements.append(temp.right.val)
                        parent[temp.right.val]=temp.val
                        level[temp.right.val]=l
                    elif temp.right is None and temp.left is not None:
                        q.append(temp.right)
                        elements.append(temp.right)
                        parent[count]=temp.val
                        level[count]=l
                        count+=1
                    
        if parent[x]!= parent[y] and level[x]==level[y]:
            return True
        else:
            return False