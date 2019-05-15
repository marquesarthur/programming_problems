


class Node(object):


    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):

    def __init__(self, node):
        self.head = node

    def add(self, node):
        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def length(self):
        cnt = 1
        current = self.head
        while current.next:
            cnt += 1
            current = current.next

        return cnt



def intersection_between(A, steps):
    k = A.length() - steps

    i = 1
    current = A.head
    while i <= k:
        current = current.next
        i += 1

    return current.value




def intersection(A, B):

    m, n = A.length(), B.length()
    if m > n:
        return intersection_between(B, m - n)
    else:
        return intersection_between(A, n - m)



a = Node(10)
b = Node(15)
c = Node(30)

x = Node(3)
y = Node(6)
z = Node(9)


b.next = c
a.next = b

z.next = b
y.next = z
x.next = y


A = LinkedList(a)
B = LinkedList(x)

print(A.length())
print(B.length())

print(intersection(A, B))