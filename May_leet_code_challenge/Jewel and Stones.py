class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel = list(J)
        stone = list(S)
        count=0
        for i in jewel:
            for j in stone:
                if i==j:
                    count+=1
        return count