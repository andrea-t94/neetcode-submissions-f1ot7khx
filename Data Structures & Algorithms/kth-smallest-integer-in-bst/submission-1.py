# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal cnt, ans
            if not node:
                return
            dfs(node.left)
            cnt -= 1
            if cnt == 0:
                ans = node.val
                return
            dfs(node.right)
        cnt = k
        ans = root.val
        dfs(root)
        return ans