# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = deque([root])
        while len(queue) > 0:
            n = len(queue)
            new_level = []
            for _ in range(n):
                node = queue.popleft()
                new_level.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
            res.append(new_level)
        return res
        
        