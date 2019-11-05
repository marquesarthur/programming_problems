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



# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        n = 1
        current = head
        while current and current.next:
            n += 1
            current = current.next

        if n <= 2:
            return head

        tail = current
        # with n I can know how many times I should apply operation
        i = 0
        aux = head
        while i < int(n / 2):
            move_to_end = aux.next
            aux.next = aux.next.next
            move_to_end.next = None
            tail.next = move_to_end
            tail = tail.next

            aux = aux.next
            i += 1

        return head



lst = ListNode.parse("1")
print(Solution().oddEvenList(lst))

lst = ListNode.parse("1->2")
print(Solution().oddEvenList(lst))

lst = ListNode.parse("1->2->3") # 1 -> 3 -> 2
print(Solution().oddEvenList(lst))

lst = ListNode.parse("1->2->3->4") # 1 -> 3 -> 2 -> 4
print(Solution().oddEvenList(lst))



# lst = ListNode.parse("1->2->3->4->5")
# print(Solution().oddEvenList(lst))

#
# lst = ListNode.parse("2->1->3->5->6->4->7")
# print(Solution().oddEvenList(lst))