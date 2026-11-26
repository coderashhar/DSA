"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def deleteGivenNode(self, node: ListNode) -> None:
        nextNode, prevNode = node.next , node.prev
        
        if nextNode is not None:
            nextNode.prev = prevNode
        prevNode.next = nextNode