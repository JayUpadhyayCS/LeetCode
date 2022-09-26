class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #can directly change one 
        #dictionary or hashtable can work very well for this problem
        dic={}
        for x in range(len(s)):
            #iterate through string and create key value pairs if missing
            #check if key already exists and check if value matches
            #check if value is reused
            
            
            
            
            #if(s[x]==t[x]):
            #    continue
            if((s[x] not in dic.keys())):
                dic.update({s[x]:t[x]})
            #if((t[x] not in dic)):
            #    dic.update({t[x]:s[x]})
                
            if(dic[s[x]] != t[x]): # or dic[t[x]] != s[x]
                return False
            
           
        for y in t:
            counter=0
            for x in dic.values():
                if y==x:
                    counter+=1
                    if counter==2:
                        return False
        return True
            
        