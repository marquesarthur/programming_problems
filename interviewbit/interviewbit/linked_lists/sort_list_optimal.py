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
    def sortList(self, A):
        def getMiddle(head):
            slowptr = head
            fastptr = head.next

            while fastptr is not None:
                fastptr = fastptr.next
                if fastptr is not None:
                    fastptr = fastptr.next
                    slowptr = slowptr.next

            return slowptr

        def mergeTwoLists(A, B):
            head = ListNode(0)
            p = head
            while A or B:
                if A and B:
                    if A.val < B.val:
                        p.next = A
                        A = A.next
                    else:
                        p.next = B
                        B = B.next
                    p = p.next
                if A == None:
                    p.next = B
                    break
                elif B == None:
                    p.next = A
                    break
            return head.next

        def sortl(A):
            if not A.next:
                return A

            mid = getMiddle(A)
            nextofmid = mid.next

            mid.next = None

            left = sortl(A)
            right = sortl(nextofmid)

            sortedList = mergeTwoLists(left, right)

            return sortedList

        return sortl(A)


A = ListNode(5).add(66).add(68).add(42).add(73).add(25).add(84).add(63). \
    add(72).add(20).add(77).add(38).add(99).add(2).add(3).add(24)

print(Solution().sortList(A))
