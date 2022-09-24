class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_ele = set()
        for num in nums:
            if num in unique_ele:
                return True
            unique_ele.add(num)
        return False