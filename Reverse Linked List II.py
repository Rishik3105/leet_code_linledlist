# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        left -= 1
        right -= 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        dummy = ListNode(0)
        curr = dummy
        for x in arr:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next
