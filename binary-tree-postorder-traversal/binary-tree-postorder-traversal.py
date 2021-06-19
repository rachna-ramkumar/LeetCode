# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        leftCall = 0
        rightCall = 1
        appendToTraversal = 2
        traversal = []
        stack = []
        stack.append((root, leftCall))
        while stack:
            node, step = stack[-1]
            if not node or step > appendToTraversal:
                stack.pop()
                continue
            stack[-1] = (node, step+1)
            if step == leftCall:
                stack.append((node.left, leftCall))
            if step == rightCall:
                stack.append((node.right, leftCall))
            if step == appendToTraversal:
                traversal.append(node.val)
        return traversal
        