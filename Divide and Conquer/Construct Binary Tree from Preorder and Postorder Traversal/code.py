# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not postorder:
            return None
        node=TreeNode(preorder[0])
        if len(preorder)==1:
            return node
        node.val=preorder[0]
        mid=postorder.index(preorder[1])
        node.left=self.constructFromPrePost(preorder[1:mid+2],postorder[0:mid+1])
        node.right=self.constructFromPrePost(preorder[mid+2:],postorder[mid+1:-1])
        return node
