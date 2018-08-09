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


class Solution:

    def mergeSortLinkedList(self, A):
        current = A
        n = 1
        while current.next:
            n += 1
            current = current.next

        mid = int(n / 2)

        head = A
        c = A
        n = c.next

        k = 1
        while k < mid:
            if n is not None:
                c = n
                n = n.next

            k += 1

        B = c.next
        c.next = None
        print(A)
        print(B)
        self.mergeSortLinkedList(A)
        self.mergeSortLinkedList(B)

        # mergeLinkedLists(A, B)

        return A

    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):

        if not A:
            return A

        self.mergeSortLinkedList(A)

        return A


A = ListNode(1).add(5).add(4).add(3)

Solution().sortList(A)
