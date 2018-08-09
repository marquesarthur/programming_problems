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


class Solution(object):

    def count(self, x):
        cX = x
        countX = 0
        while cX:
            countX += 1
            cX = cX.next

        return countX

    def getIntersectionNode(self, x, y):
        cX = x
        cY = y

        countX = self.count(x)
        countY = self.count(y)

        if countX < countY:
            for i in range(countY - countX):
                cY = cY.next
        else:
            for i in range(countX - countY):
                cX = cX.next

        for i in range(min(countX, countY)):
            if cX is cY:
                return cX

            cX = cX.next
            cY = cY.next

        return None





x = LinkedList(5).add(4)
y = LinkedList(1)
z = LinkedList(6).add(3)

cX = x
while cX.next:
    cX = cX.next

cY = y
while cY.next:
    cY = cY.next

cY.next = z
cX.next = z

print(Solution().getIntersectionNode(x, y))



