class swapin:
    class Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def insert(self, value):
        new_node = self.Node(value)
        if self._head is None:
            self._head = new_node
        else:
            temp = self._head
            while temp._next:
                temp = temp._next
            temp._next = new_node
        self._size += 1

    def swap_pairs(self):
        dummy = self.Node(0)
        dummy._next = self._head
        prev = dummy
        while prev._next and prev._next._next:
            first = prev._next
            second = first._next
            first._next = second._next
            second._next = first
            prev._next = second
            prev = first
        self._head = dummy._next

    def display(self):
        temp = self._head
        while temp:
            print(temp._element, end=" ")
            temp = temp._next
        print()

if __name__ == "__main__":
    s = swapin()
    nums = list(map(int, input("Enter your list: ").split()))
    for i in nums:
        s.insert(i)
    s.swap_pairs()
    print("Swapped list:")
    s.display()
