# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    # @return an integer
    def lPalin(self, A):
        head = A
        fast = head
        prev = None
        # reversing the first half of the list
        while fast and fast.next:
            fast = fast.next.next
            head.next, prev, head = prev, head, head.next
        # if the number of nodes if odd skip the middle one
        tail = head.next if fast else head
        # Compare the tail and prev elements while setting
        # the list to its original state
        is_palindrome = True
        while prev and is_palindrome:
            is_palindrome = is_palindrome and (tail.val == prev.val)
            prev.next, head, prev = head, prev, prev.next
            tail = tail.next
        if is_palindrome == True:
            return 1
        else:
            return 0

Solution().lPalin(ListNode(1).add(5).add(1))



