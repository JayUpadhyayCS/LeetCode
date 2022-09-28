# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dictionary={}
        index=0
        while(head):
            index+=1
            if head in dictionary.keys():
                return head
            else:
                dictionary[head]=index
            head=head.next
        return None