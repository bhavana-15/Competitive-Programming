# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if head.next==None:
            return TreeNode(head.val)
        slow,fast=head,head
        cur=head
        while(fast and fast.next):
            cur=slow
            slow=slow.next
            fast=fast.next.next
        node=TreeNode(slow.val)
        cur.next=None
        node.left=self.sortedListToBST(head)
        right=slow.next

        node.right=self.sortedListToBST(right)
        return node
