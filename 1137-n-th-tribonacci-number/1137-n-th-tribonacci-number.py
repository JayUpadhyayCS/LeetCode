class Solution:
    def tribonacci(self, n: int) -> int:
        if(n<=0):
            return 0
        elif n==1:
            return 1
        mem=[0]*3
        mem[1]=1
        mem[2]=1
        m=2
        while(n!=m):
            m+=1
            mem[m%3]=mem[2]+mem[1]+mem[0]
            
        return mem[m%3]
        
            
        