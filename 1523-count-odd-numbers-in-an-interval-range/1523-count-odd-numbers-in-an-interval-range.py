class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # 3 cases
        # Odd Odd 9-17= 17-9=8/2=4  9-11-13-15-17 +1?
        if low%2 or high%2: #if both odd
            return ((high-low)//2) +1
        # Even Even 16, 10=6/2=3 -- 11-13-15
        else:#lif !(low%2) and (high%2)
            return ((high-low)//2)
        # Even Odd  17/10=7//2=3.5=4=11,13-15-17
        #elif low%2 or high%2:
        #    return ((high-low)//2) +1
        
        