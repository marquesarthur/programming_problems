# Split the list into buckets of length K and then reverse each of them.
# After this you have to concatenate the buckets and return the list.
# To split the list into buckets of length K, use 2 pointers that are K elements afar. To reverse a linked list check this.


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
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if A is None:
            return None

        _previous = None
        _next = None
        _current = A # Initializes the list

        count = 0
        # current starts at the head of the array
        while count < B:
            _next = _current.next # gets the next element and stores it in aux 1
            _current.next = _previous  # makes the head of the array point to None or the excluded element
            _previous = _current # gets the excluded element
            _current = _next # reduces the list size by 1 this is a pointer to the last element in the list


            count += 1

        if _next:
            A.next = self.reverseList(_next, B)

        return _previous




A = ListNode(6).add(10).add(0).add(3).add(4).add(8)


print(Solution().reverseList(A, 3))