import heapq


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

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def __merge_sorted_linked_lists(self, A, B):
        dummy = ListNode("dummy")
        current = dummy

        cA = A
        cB = B

        while cA and cB:
            if cA.val < cB.val:
                current.next = ListNode(cA.val)
                cA = cA.next
            else:
                current.next = ListNode(cB.val)
                cB = cB.next

            current = current.next

        while cA:
            current.next = ListNode(cA.val)
            cA = cA.next
            current = current.next

        while cB:
            current.next = ListNode(cB.val)
            cB = cB.next
            current = current.next

        return dummy.next

    def __merge(self, A):
        A_prime = []
        i = 0
        while i < len(A):
            head_i = A[i]
            if i + 1 < len(A):
                A[i] = self.__merge_sorted_linked_lists(A[i], A[i + 1])

            A_prime.append(A[i])
            i += 2

        return A_prime

    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        # 1st while len(A) != 1
        # merge half of the linked lists
        # Once everythin is merged
        # convert to list
        # sort and transform back to list
        # there may be a way to do that without transforming

        if not A:
            return A

        while len(A) > 1:
            A = self.__merge(A)

        return A[0]


A = [
    ListNode.parse("1 -> 10 -> 20"),
    ListNode.parse("4 -> 11 -> 13"),
    ListNode.parse("3 -> 8 -> 9")
]
print(Solution().mergeKLists(A))
