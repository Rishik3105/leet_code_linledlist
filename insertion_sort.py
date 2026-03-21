class InsertionSortLinkedList:
    class _Node:
        __slots__ = 'element', 'next'
        def __init__(self, element, next=None):
            self.element = element
            self.next = next
    def __init__(self):
        self._head = None
        self._size = 0
    def __len__(self):
        return self._size
    def insert(self, value):
        new = self._Node(value)

        if self._head is None:
            self._head = new
        else:
            temp = self._head
            while temp.next:
                temp = temp.next
            temp.next = new
        self._size += 1
    def sort(self):
        sorted_head = None 
        current = self._head
        while current:
            next_node = current.next
            if sorted_head is None or current.element < sorted_head.element:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.element < current.element:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node
        self._head = sorted_head
    def display(self):
        temp = self._head
        while temp:
            print(temp.element, end=" ")
            temp = temp.next
        print()
if __name__ == "__main__":
    nums = list(map(int, input("Enter your sequence: ").split()))
    ll = InsertionSortLinkedList()
    for num in nums:
        ll.insert(num)
    print("Original list:")
    ll.display()
    ll.sort()
    print("Sorted list:")
    ll.display()
    print("Size:", len(ll))
