"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def insertBeforeHead(self, head: ListNode, X: int) -> ListNode:
        newNode = ListNode(X)
        temp = head
        temp.prev = newNode
        newNode.next = temp
        head = newNode

        return head
