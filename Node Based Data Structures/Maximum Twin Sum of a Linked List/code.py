# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=fast=head
        st=[]
        maxsum=0
        while fast and fast.next:
            fast=fast.next.next
            st.append(slow)
            slow=slow.next
        while slow:
            maxsum=max(maxsum,st.pop().val+slow.val)
            slow=slow.next
        return maxsum
