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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode("dummy")
        dummy.next = head

        slow = dummy
        fast = dummy

        i = 0
        while fast.next is not None:
            fast = fast.next
            i += 1
            if i > n:
                slow = slow.next


        if n <= i:
            slow.next = slow.next.next
        return dummy.next


# print(Solution().removeNthFromEnd(ListNode.parse("1->2->3->4->5"), 2))
print(Solution().removeNthFromEnd(ListNode.parse("1->2->3->4->5"), 5))
print(Solution().removeNthFromEnd(ListNode.parse("1->2->3->4->5"), 6))