class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
     #sorting is nlogn
    #can do linear time but need a hash to store
    
        diction={}
        for num in nums:
            if diction.get(num)==None:
                diction.update({num: True})
            else:
                return True
        return False
    
            