class Solution:
    def fib(self, n: int) -> int:
        if(n<=0):
            return 0
        mem=[0]*2
        mem[1]=1
        m=1
        while(n!=m):
            m+=1
            mem[m%2]=mem[1]+mem[0]
            
        return mem[m%2]
        
            
        