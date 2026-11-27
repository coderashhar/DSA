"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def insertBeforeGivenNode(self, node: ListNode, X: int) -> None:
        newNode = ListNode(X)

        prevNode = node.prev
        prevNode.next = newNode
        newNode.prev = prevNode
        newNode.next = node
        node.prev = newNode

