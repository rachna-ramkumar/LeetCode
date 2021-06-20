# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, min = -math.inf, max = math.inf):
            if not node:
                return True
            if node.val <= min or node.val >= max:
                return False
            return (dfs(node.right, node.val, max) and dfs(node.left, min, node.val))
        return dfs(root)