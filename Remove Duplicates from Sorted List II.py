# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        unique = []
        n = len(arr)
        for i in range(n):
            if (i == 0 or arr[i] != arr[i - 1]) and \
               (i == n - 1 or arr[i] != arr[i + 1]):
                unique.append(arr[i])
        dummy = ListNode(0)
        curr = dummy

        for num in unique:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next
