class Solution:
    def findComplement(self, num: int) -> int:
        bin_num=bin(num)
        l1=list(bin_num)
        for i in range(2,len(l1)):
            if l1[i]=="1":
                l1[i]="0"
            else:
                l1[i]="1"
        bin_res="".join(l1)
        res=int(bin_res, 2)
        return res