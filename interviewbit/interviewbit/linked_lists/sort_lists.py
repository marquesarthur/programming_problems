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

    def mergeLinkedLists(self, A, B):
        head = None
        cA = A
        cB = B

        # Find who is the head
        if cA.val < cB.val:
            head = cA
            cA = cA.next
            head.next = None
        else:
            head = cB
            cB = cB.next
            head.next = None

        current = head

        # Walk comparing values in the list
        while cA is not None and cB is not None:
            if cA.val < cB.val:
                current.next = cA
                cA = cA.next
                current = current.next
                current.next = None
            else:
                current.next = cB
                cB = cB.next
                current = current.next
                current.next = None

        # fill in remaining values with A
        while cA is not None:
            current.next = cA
            cA = cA.next
            current = current.next
            current.next = None

        # fill in remaining values with B
        while cB is not None:
            current.next = cB
            cB = cB.next
            current = current.next
            current.next = None

        return head

    def mergeSortLinkedList(self, A):
        current = A
        n = 1
        while current.next:
            n += 1
            current = current.next

        if n == 1:
            return A

        mid = int(n / 2)

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
        A = self.mergeSortLinkedList(A)
        B = self.mergeSortLinkedList(B)

        result = self.mergeLinkedLists(A, B)

        return result

    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):

        if not A:
            return A



        return self.mergeSortLinkedList(A)


A = ListNode(1).add(5).add(4).add(3)
A = ListNode(5).add(66).add(68).add(42).add(73).add(25).add(84).add(63).\
    add(72).add(20).add(77).add(38).add(99).add(2).add(3).add(24)

print(Solution().sortList(A))
