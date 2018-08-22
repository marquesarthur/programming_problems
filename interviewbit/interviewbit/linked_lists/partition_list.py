# Definition for singly-linked list.
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
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):

        # find first next which is greater or equal to X
        # leave pointer there
        # walk in the reminder or the list moving pointers to placeholder
        # return

        # I may have to have a dummy
        dummy = ListNode("dummy")
        dummy.next = A

        current = dummy
        while current.next and current.next.val < B:
            current = current.next
        replacer = current

        to_be_replaced = replacer
        while to_be_replaced.next:
            if to_be_replaced.next.val < B:
                aux = to_be_replaced.next
                to_be_replaced.next = to_be_replaced.next.next
                aux.next = current.next
                current.next = aux
                current = aux
            else:
                to_be_replaced = to_be_replaced.next

        return dummy.next

# A = ListNode.parse("1->4->3->2->5->2")
# B = 3
# print(Solution().partition(A, B))

A = ListNode.parse("4->3->1->5->1")
B = 2
print(Solution().partition(A, B))



