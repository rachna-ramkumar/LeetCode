# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, level, result):
        if root is None:
            return
        if level >= len(result):
            result.append([])
        result[level].append(root.val)
        self.dfs(root.left, level + 1, result)
        self.dfs(root.right, level + 1, result)
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.dfs(root, 0, result)
        for level in range(1, len(result), 2):
            result[level].reverse()
        return result
                
        
        