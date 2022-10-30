class Solution:
    def average(self, salary: List[int]) -> float:
        #sort then take 1:-1
        maxi=salary[0]
        mini=salary[0]
        summation=0
        for x in salary:
            if(x>maxi):
                maxi=x
            elif x<mini:
                mini=x
            summation+=x
            print (summation)

        return ((summation-maxi-mini)/(len(salary)-2))