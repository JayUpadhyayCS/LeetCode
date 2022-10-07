class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini= float('inf')
        maxi=0
        answer=0
        for x in prices:
            if x<mini:
                mini=x
            elif x-mini>maxi:
                maxi=x-mini
        return maxi
     #Have a max that changes
    # Compute max profit
    
    #Create an empty array
    # for each value check 
    #
    #
    #

        