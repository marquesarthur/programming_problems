# Definition for singly-linked list.
class ListNode(object):
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

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head
        temp = head
        size = 1
        while temp.next:
            size += 1
            temp = temp.next
        temp.next = head
        k %= size
        for i in range(size - k):
            head = head.next
            temp = temp.next
        temp.next = None
        return head







#
input = ListNode.parse("1->2->3->4->5")
k = 2
print(Solution().rotateRight(input, k))
#
# input = ListNode.parse("1->2->3->4->5")
# k = 5
# print(Solution().rotateRight(input, k))
#
#
# input = ListNode.parse("1")
# k = 5
# print(Solution().rotateRight(input, k))
#
#
#
#
# input = ListNode.parse("0->1->2")
# k = 4
# print(Solution().rotateRight(input, k))

#
# input = ListNode.parse("1->2")
# k = 1
# print(Solution().rotateRight(input, k))