# 1) Break the list from middle into 2 lists.
# 2) Reverse the latter half of the list.
# 3) Now merge the lists so that the nodes alternate.

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

    def findMiddleNode(self, A):
        slow = A
        fast = A

        if not slow.next:
            return None

        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverseList(self, A):

        current = A
        head, _next = None, None

        while current:
            _next = current.next
            current.next = head
            head = current
            current = _next

        return head

    def count(self, A):
        c = 0
        current = A
        while current:
            current = current.next
            c += 1

        return c

    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        # 1st I have to find the middle
        # 2nd I have to reverse from the middle to the last
        # then I walk inserting head, reversed until I reach the end
        current = A
        middle = self.findMiddleNode(A)

        n = self.count(A)

        if not middle:
            return A

        while current.next != middle:
            current = current.next

        if current.next == middle:
            current.next = None

        last = None
        if n % 2 == 1:
            last = middle
            middle = middle.next
            last.next = None

        middle = self.reverseList(middle)

        head = A
        cHead, cMiddle = head, middle

        while cHead and cMiddle:
            aux = cMiddle
            _next = cMiddle.next

            aux.next = cHead.next
            cHead.next = aux
            cMiddle = _next
            cHead = cHead.next.next

        if last:
            cHead = head
            while cHead.next:
                cHead = cHead.next

            cHead.next = last

        return head


A = ListNode(1).add(2).add(3).add(4).add(5).add(6).add(7)
# A = ListNode.parse("12 -> 6 -> 75 -> 98 -> 58 -> 81 -> 30 -> 101 -> 87 -> 40 -> 70 -> 45 -> 41 -> 20 -> 66 -> 1 -> 96 -> 35 -> 51 -> 79 -> 61 -> 48 -> 99 -> 11 -> 32 -> 88 -> 60 -> 18 -> 42 -> 29 -> 13 -> 91 -> 85 -> 10 -> 33 -> 52 -> 84 -> 4 -> 94 -> 46 -> 23 -> 82 -> 59 -> 38 -> 97 -> 17 -> 14 -> 90 -> 54 -> 69 -> 57 -> 74 -> 73 -> 39")

print(Solution().reorderList(A))
