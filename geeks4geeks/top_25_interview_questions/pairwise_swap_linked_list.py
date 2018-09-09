

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, val):
        node = ListNode(val)
        current = self
        while current.next is not None:
            current = current.next
        current.next = node
        return self

    def __str__(self):
        result = []
        current = self
        while current is not None:
            result.append(str(current.val))
            current = current.next

        return " -> ".join(result)

    @staticmethod
    def parse(str):
        numbers = str.split("->")
        head = None
        for i in numbers:
            i = int(i.strip())
            if not head:
                head = ListNode(i)
            else:
                head = head.add(i)

        return head

# METHOD 1 (Iterative)
# If there are 2 or more than 2 nodes in Linked List then swap the first two nodes and recursively call for rest of the list.
def swap(head):


    dummy = ListNode("dummy")
    dummy.next = head

    current = dummy


    while current.next and current.next.next:
        a = current.next
        b = current.next.next

        a.next = b.next
        b.next = a

        current.next = b
        current = current.next.next

    return dummy.next


# METHOD 2 (Recursive)
# Start from the head node and traverse the list. While traversing swap data of each node with its next node’s data.
def swap_recursive(head):
    if head is None:
        return None


    if head.next is not None:
        a = head
        b = head.next

        a.next = swap_recursive(b.next)
        b.next = a
        head = b


    return head








A = ListNode.parse("1 -> 2 -> 3 -> 4 -> 5")
B = ListNode.parse("1 -> 2 -> 3 -> 4 -> 5 -> 6")
print(swap(A))
print(swap_recursive(B))