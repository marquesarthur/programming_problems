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
    def reverseList(self, A):

        # 3 -> 4 >- 5 -> 1
        current = A # 3 -> 4 >- 5 -> 1
        head, _next = None, None

        while current:
            _next = current.next # next = 5 -> 1
            current.next = head # current =  -> None
            head = current # prev = 3 -> None
            current = _next  # current =  4 >- 5 -> 1

        return head


A = ListNode(1).add(5).add(4).add(3)


print(Solution().reverseList(A))
