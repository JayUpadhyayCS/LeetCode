class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index=0
        if len(s)==0:
            return True
        for x in t:
            if x==s[index]:
                index+=1
            if(index>=len(s)):
                return True
        return False