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
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if not A:
            return A

        current = A
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return A
