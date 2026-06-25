# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        less = []
        greater = []
        while head:
            if head.val < x:
                less.append(head.val)
            else:
                greater.append(head.val)
            head = head.next
        result = less + greater
        dummy = ListNode(0)
        curr = dummy
        for num in result:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next
