# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        # search: apply BS property
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # swap
            # base cases covers as well leaves
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # in case both, I want right-most left subtree
            cur = root.left
            while cur.right:
                cur = cur.right
            root.val = cur.val
            root.left = self.deleteNode(root.left, root.val)
        return root
