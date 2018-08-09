# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    def reverse(self, A):
        current = A

        head, _next = None, None

        while current:
            _next = current.next
            current.next = head
            head = current
            current = _next

        return head

    def copy(self, A):
        cA = A

        head = ListNode(cA.val)
        cNew = head
        while cA.next:
            k = ListNode(cA.next.val)
            cNew.next = k
            cA = cA.next
            cNew = cNew.next

        return head

    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):

        # 1st reverse list
        B = self.copy(A)
        print(B)

        C = self.reverse(A)
        print(C)



        # 2nd walk in list comparing values
        cB = B
        cC = C
        while cB and cC:
            if cB.val != cC.val:
                return 0
            cB = cB.next
            cC = cC.next

        return 1


Solution().lPalin(ListNode(1).add(5).add(4).add(3))



