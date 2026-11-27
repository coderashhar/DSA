"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""
class Solution:
    def arrayToDoublyLinkedList(self, arr):
        if len(arr) == 0:
            return None
        
        head = ListNode(arr[0])

        if len(arr) == 1:
            return head

        temp = head
        for i in range(1, len(arr)):
            newNode = ListNode(arr[i])
            temp.next = newNode
            newNode.prev = temp
            temp = temp.next
        
        return head
            
            
