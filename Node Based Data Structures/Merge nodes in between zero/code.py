# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp.next:
            prev=temp
            if temp.next.val!=0:
                temp.val+=temp.next.val
                temp.next=temp.next.next
            else:
                temp=temp.next
        prev.next=None
        return head
