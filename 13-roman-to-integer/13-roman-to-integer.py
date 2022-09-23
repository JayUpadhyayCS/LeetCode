# IV
# MCMXCIV
class Solution:
    def romanToInt(self, s: str) -> int:
        dick={'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prev=1001
        i=0
        for x in s:
            if prev < dick[x]:
                i= i - 2*prev
            i= i+dick[x]
            prev=dick[x]
        return i
    
        
        
        
        