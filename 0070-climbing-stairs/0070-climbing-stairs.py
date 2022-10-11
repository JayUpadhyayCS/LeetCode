class Solution:

    def climbStairs(self, n: int) -> int:
        #initialization
        if(n<=0):
            return 0
        elif n==1:
            return 1
        arr=[0]*n
        arr[0]=1
        arr[1]=2
        return self.helper(n-1,arr)
    def helper(self, n: int, arr: list) -> int:  
        if(arr[n]==0):
            arr[n]=self.helper(n-1,arr)+self.helper(n-2,arr)
        return arr[n]
        #4
# 1. 1 step + 1 step + 1 step +1
# 2. 1 step + 2 steps+1
# 3. 2 steps + 1 step+1
# 4. 1+1+2
# 5. 2+2


# 1. 1 step + 1 step + 1 step +1 +1

# 2. 1 step + 2 steps+1
# 3. 2 steps + 1 step+1
# 4. 1+1+2
# 5. 2+2
# 6. 