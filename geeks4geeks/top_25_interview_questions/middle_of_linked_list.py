# Method 1:
# Traverse the whole linked list and count the no. of nodes.
# Now traverse the list again till count/2 and return the node at count/2.
#
# Method 2:
# Traverse linked list using two pointers. Move one pointer by one and other pointer by two.
# When the fast pointer reaches end slow pointer will reach middle of the linked list.




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

def middle(head):
    n = 0
    if not head:
        return None

    current = head
    while current:
        n += 1
        current = current.next

    j = int(n / 2)
    i = 0
    current = head
    while current and i < j:
        i += 1
        current = current.next

    return current.val




A = ListNode.parse("1 -> 2 -> 3 -> 4 -> 5")
B = ListNode.parse("1 -> 2 -> 3 -> 4 -> 5 -> 6")
print(middle(A))
print(middle(B))