# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        if not head:
            return head
        dummy = ListNode(0)  # sorted list dummy head
        curr = head
        while curr:
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            next_node = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = next_node
        return dummy.next
