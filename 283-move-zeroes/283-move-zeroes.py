class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        itr,z, length= 0,0,len(nums)
        
        while(itr<length):
            if nums[z] == 0 and nums[itr]!=0:
                nums[z],nums[itr] = nums[itr],nums[z]
            elif nums[z]!=0 and nums[itr]==0:
                z+=1
            else:
                itr+=1
            
            
            