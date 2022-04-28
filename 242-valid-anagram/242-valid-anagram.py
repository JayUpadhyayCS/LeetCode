class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #log each of the characters 
        #check each of values are true/found
        diction={}
        for c in s:
            if diction.get(c)==None:
                diction.update({c:1})
            else:
                #probably doesnt work
                diction[c]+=1
        for c in t:
            if diction.get(c)==None:
                return False
            else:
                #probably doesnt work
                diction[c]-=1
        for v in diction.values():
            if v != 0:
                return False
        return True

        