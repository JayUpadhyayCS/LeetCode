class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic={}
        length=0
        for x in s:
            if x not in dic:
                dic[x]=1
            else:
                dic[x]+=1
        val= 0
        for x in dic.values():
            if x%2==0:
                length+=x
            elif x>1:
                length+=x-1
                val=1
            else:
                val=1
        return val+length
                