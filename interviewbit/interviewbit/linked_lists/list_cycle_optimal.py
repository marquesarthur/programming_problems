# Definition for singly-linked list.
# If you detect a cycle, the meeting point is definitely a point within the cycle.
#
# Can you determine the size of the cycle ? ( Easy ) Let the size be k.
# Fix one pointer on the head, and another pointer to kth node from head.
# Now move them simulataneously one step at a time. They will meet at the starting point of the cycle.
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
        count = 0
        limit = 10
        while current is not None:
            if count >= limit:
                result.append("..")
                break
            result.append(str(current.val))
            current = current.next
            count += 1

        return " -> ".join(result)

class Solution:
    class Solution:
        # @param A : head node of linked list
        # @return the first node in the cycle in the linked list
        def detectCycle(self, A):
            slow, fast = A.next, None
            if slow:
                fast = slow.next
            while fast and fast != slow:
                if fast.next and fast.next.next:
                    slow = slow.next
                    fast = fast.next.next
                else:
                    fast = fast.next
            if fast == slow:
                slow = A
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
            return fast



class SolutionMarking:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        current = A
        ListNode.visited = None # this dynamically adds an attribute to the class
        while current:

            if current.visited is None:
                current.visited = True
            else:
                return current

            current = current.next

        return None



x = ListNode(5).add(4)
y = ListNode(1)
tail = x
while tail.next:
    tail = tail.next

tail.next = y
y.next = x

print(SolutionMarking().detectCycle(x).val)



