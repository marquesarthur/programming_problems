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


class Solution:

    # @param A : head node of linked list
    # @return the head node in the linked list
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        start = ListNode('dummy')
        start.next = A
        current = start
        while current.next and current.next.next:
            current.next = self.swap(current.next, current.next.next)
            current = current.next.next
        return start.next

    def swap(self, node1, node2):
        node1.next = node2.next
        node2.next = node1
        return node2


# A = ListNode.parse("28 -> 34 -> 48 -> 74 -> 42 -> 49 -> 37 -> 59 -> 97 -> 96 -> 73 -> 44 -> 39 -> 50 -> 80 -> 30 -> 95 -> 26 -> 94 -> 88 -> 87 -> 84 -> 57 -> 47 -> 100 -> 56 -> 69 -> 27 -> 58 -> 2 -> 64 -> 86 -> 8 -> 43 -> 41 -> 32 -> 67 -> 51 -> 53 -> 101 -> 7 -> 76 -> 92 -> 45 -> 83 -> 6 -> 46 -> 40 -> 16 -> 66 -> 91 -> 1 -> 63 -> 89 -> 90 -> 4 -> 52 -> 65 -> 3 -> 70 -> 62 -> 29 -> 71 -> 15 -> 22 -> 93 -> 24 -> 25 -> 61 -> 82 -> 54 -> 60 -> 81 -> 14 -> 33 -> 85 -> 13 -> 17 -> 20 -> 31 -> 18 -> 79 -> 68 -> 10 -> 38 -> 11 -> 78 -> 72 -> 55 -> 36 -> 19 -> 99 -> 77 -> 5 -> 12 -> 35 -> 23 -> 21 -> 98")
A = ListNode.parse("28 -> 34 -> 48 -> 74 -> 42")
print(Solution().swapPairs(A))

