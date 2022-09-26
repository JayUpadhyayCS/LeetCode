class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ=sum(nums)
        lsum=0
        for x in range(len(nums)):
            summ-=nums[x]
            if(summ==lsum):
                return x
            lsum+=nums[x]
        return -1
        