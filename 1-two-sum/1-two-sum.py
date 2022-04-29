class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - index = new arr
        nums1=[]
        for num in range(len(nums)):
            for num1 in range(len(nums1)):
                if nums[num] == nums1[num1]:
                    return num1,num
            #It doesnt exist in second array
            nums1.append(target-nums[num])
            