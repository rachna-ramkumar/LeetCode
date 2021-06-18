"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        self.dfs(root, result)
        return result
    
    def dfs(self, node, result):
        if not node:
            return None
        else:
            for child in node.children:
                self.dfs(child, result)
            result.append(node.val)
        
        