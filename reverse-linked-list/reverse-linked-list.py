# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        previousNode, currentNode = None, head
        while currentNode:
            currentNode.next, previousNode, currentNode = previousNode, currentNode, currentNode.next
        return previousNode
        
        
        