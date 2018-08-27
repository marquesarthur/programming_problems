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


# 1. Create a head comparing the head of each node in A
# 2. init head and tail of the response as None
# 3. pop min list from the heap
# 4. add that new node to result and update tail
# 5. push next of min list if there is one
# 6. repeat while heap is not empty
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        h = [l for l in A if l is not None]
        heapq.heapify(h)
        res_head = res_tail = None

        while len(h) > 0:
            n = heapq.heappop(h)
            new_node = ListNode(n.val)
            if res_head is None:
                res_head = res_tail = new_node
            else:
                res_tail.next = new_node
                res_tail = new_node

            if n.next is not None:
                heapq.heappush(h, n.next)

        return res_head


A = [
    ListNode.parse("1 -> 10 -> 20"),
    ListNode.parse("4 -> 11 -> 13"),
    ListNode.parse("3 -> 8 -> 9")
]
print(Solution().mergeKLists(A))
