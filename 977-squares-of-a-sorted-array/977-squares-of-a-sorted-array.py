class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left,right=0,len(nums)-1
        nums2=[]
        while(left<=right):
            if(nums[left]**2 > nums[right]**2):
                nums2.append(nums[left]**2)
                left+=1
            else:
                nums2.append(nums[right]**2)
                right-=1
        num2=nums2.reverse()
        return nums2        