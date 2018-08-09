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

# Use Hashing:
# Traverse the list one by one and keep putting the node addresses in a Hash Table.
# At any point, if NULL is reached then return false and if next of current node points to any of the previously stored nodes in Hash then return true.

# Mark Visited Nodes:
# This solution requires modifications to basic linked list data structure.  Have a visited flag with each node.  Traverse the linked list and keep marking visited nodes.  If you see a visited node again then there is a loop. This solution works in O(n) but requires additional information with each node.
# A variation of this solution that doesn’t require modification to basic data structure can be implemented using hash.  Just store the addresses of visited nodes in a hash and if you see an address that already exists in hash then there is a loop.

class Solution:
    def firstInCycle(self, pointInClycle, A):

        current = pointInClycle
        count = 0
        while current.next != pointInClycle:
            current = current.next
            count += 1

        c = A
        kth = A
        i = 0
        while i <= count:
            kth = kth.next
            i += 1

        while c != kth:
            c = c.next
            kth = kth.next

        return c

    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):

        # start with a slow pointer
        # have a faster pointer

        # find when they collide
        # if fast pointer is none, then no cycle is found

        current = A
        slow = current
        fast = current
        while slow and fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return self.firstInCycle(slow, A)

        return None




x = ListNode(5).add(4)
y = ListNode(1)
tail = x
while tail.next:
    tail = tail.next

tail.next = y
y.next = x

print(Solution().detectCycle(x).val)



