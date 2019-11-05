class LinkedList(object):

    def __init__(self, val):
        self.value = val
        self.next = None

    # O(n)
    def add(self, val):
        head = self
        current = head
        while current.next:
            current = current.next

        node = LinkedList(val)
        current.next = node
        return self

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.value))
            current = current.next

        return " -> ".join(result)

    def find_middle(self):

        slow = self
        fast = self.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self):

        current = self
        head, _next = None, None

        while current:
            _next = current.next
            current.next = head
            head = current
            current = _next

        return head



x = LinkedList(5).add(4).add(6).add(4).add(3)
print(x)
print(x.find_middle())
print(x.reverse())



class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = LinkedList("dummy")
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