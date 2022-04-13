# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right, ver= 0,n,100000
        
        
        while(left<=right):
            center=(left+right)//2
            if isBadVersion(center):
                right=center-1
                ver=center
            else:
                left=center+1
        return ver