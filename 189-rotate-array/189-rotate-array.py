class Solution:
    #how to use no space but track if we get to same element again? increment touched vls
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        #iterate by two or 3
        k%=length
        x=0
        counter=length-1
        nextNum=k
        #need to check if we touch same element again
        temp=nums[nextNum]
        nums[nextNum]=nums[0]
        nextNum+=k
        nextNum%=length

        while(counter):
            #need var to keep loc
            
            if(nextNum>x ): #or(nextNum==0 and counter==1 )
                
                temp2=nums[nextNum]
                nums[nextNum]=temp
                counter-=1
                temp=temp2
                nextNum+=k
                nextNum%=length
            else:
                x+=1
                
                temp2=nums[(nextNum+1)%length]
                nums[nextNum]=temp
                counter-=1
                temp=temp2
                nextNum+=1 +k
                nextNum%=length
        