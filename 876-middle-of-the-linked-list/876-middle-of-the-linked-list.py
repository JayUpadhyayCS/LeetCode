# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2=head
        counter=1
        while head2.next !=None:
            head2=head2.next
            counter+=1
        counter=counter//2
        while(counter>0):
            counter-=1
            head=head.next
        return head
        