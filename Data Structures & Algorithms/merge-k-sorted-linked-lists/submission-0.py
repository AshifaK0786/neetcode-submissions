# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists):
        arr = []

        for head in lists:
            while head:
                arr.append(head.val)
                head = head.next

        arr.sort()

        dummy = ListNode()
        temp = dummy

        for x in arr:
            temp.next = ListNode(x)
            temp = temp.next

        return dummy.next