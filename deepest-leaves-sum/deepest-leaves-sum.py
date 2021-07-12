class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        next_level = deque([root,])
        
        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()
            
            for node in curr_level:
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        
        return sum([node.val for node in curr_level])