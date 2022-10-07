class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini= float('inf')
        
        previ=0
        profit=0
        for x in prices:
            if float('inf')==mini:
                mini=x
            elif(x-mini>profit):
                profit=x-mini
            if(x<mini):
                mini=x
        return profit
     #Have a max that changes
    # Compute max profit
    
    #Create an empty array
    # for each value check 
    #
    #
    #

        