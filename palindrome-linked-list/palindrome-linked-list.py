# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        out = []
        while head:
            out.append(head.val)
            head = head.next
        return out == out[::-1]
            
        