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
    def parse(string):
        values = [i.strip() for i in string.split("->")]
        if not values:
            return None

        head = ListNode(values[0])
        for value in values[1:len(values)]:
            head.add(value)
        return head



class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if not A:
            return A

        # It is sorted so that means that I can look at the next
        # If current.val == next.val
        # Stores val into aux
        # delete while current.next == val
        # Check if head is equals to val
        # updates head
        # otherwise, move ahead

        head = ListNode("dummy")
        head.next = A

        # dummy -> 1 -> 2 -> 3
        current = head
        while current and current.next:
            aux = current.next.val  # 1
            _next = current.next.next

            remove = False
            while _next and _next.val == aux:
                remove = True

                _next = _next.next

            if remove:
                current.next = _next
            else:
                current = current.next


        return head.next


A = ListNode.parse("1 -> 1 -> 1 -> 2 -> 2 -> 2 ->  3 -> 3")
# A = ListNode.parse("1 -> 2 -> 3")
# A = ListNode(1).add(2).add(3).add(3).add(4).add(4).add(5)

print(Solution().deleteDuplicates(A))