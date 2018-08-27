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
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        carry_over = 0

        cA = A
        cB = B
        result = ListNode("dummy")
        current = result
        while cA and cB:
            partial = (cA.val + cB.val + carry_over)
            carry_over = int(partial / 10)
            value = int(partial % 10)
            current.next = ListNode(value)
            current = current.next
            cA = cA.next
            cB = cB.next

        # Threat case where A or B have different sizes
        while cA:
            partial = (cA.val + carry_over)
            carry_over = int(partial / 10)
            value = int(partial % 10)
            current.next = ListNode(value)
            current = current.next
            cA = cA.next

        while cB:
            partial = (cB.val + carry_over)
            carry_over = int(partial / 10)
            value = int(partial % 10)
            current.next = ListNode(value)
            current = current.next
            cB = cB.next

        if carry_over > 0:
            current.next = ListNode(carry_over)

        return result.next


A = ListNode.parse("2 -> 4 -> 3")
B = ListNode.parse("5 -> 6 -> 4")

print(Solution().addTwoNumbers(A, B))
