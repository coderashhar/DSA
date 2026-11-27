"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def insertBeforeKthPosition(self, head: ListNode, X: int, k: int) -> ListNode:
        newNode = ListNode(X)

        if k == 1:
            head.prev = newNode
            newNode.next = head
            return newNode
        
        temp = head
        while temp.next is not None and k > 2:
            temp = temp.next
            k -= 1
            
        temp2 = temp.next
        temp.next = newNode
        newNode.prev = temp
        newNode.next = temp2
        temp2.prev = newNode

        return head
        