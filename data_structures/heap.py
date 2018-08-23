# Based on
# http://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapImplementation.html
# other good resources:
#   https://medium.com/basecs/heapify-all-the-things-with-heap-sort-55ee1c93af82
#   https://medium.com/basecs/learning-to-love-heaps-cef2b273a238


# Common methods are in BinHeap
# Specific cases are in MinHeap and MaxHeap
# MinHeap has smallest values at A[1]
# MaxHeap has largest values at A[1]

import abc


class BinHeap(object):
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def insert(self, value):
        self.heap_list.append(value)
        self.size += 1
        self.bubbleUp(self.size)

    def bubbleUp(self, i):
        while i // 2 > 0:  # floor division, will always return an int
            parent = self.heap_list[i // 2]
            if self.compare(self.heap_list[i], parent):
                aux = parent
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = aux

            i = i // 2

    def pop(self):
        result = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]  # move largest element to first index
        self.size -= 1  # decrease heap size
        self.heap_list.pop()  # delete last index which previously contained the largest element
        self.bubbleDown(1)  # start to bubble down the largest element
        return result

    def bubbleDown(self, i):
        while (i * 2 <= self.size):
            mc = self.child(i)
            if self.compare(self.heap_list[mc], self.heap_list[i]):
                temp = self.heap_list[mc]
                self.heap_list[mc] = self.heap_list[i]
                self.heap_list[i] = temp

            i = mc

    @abc.abstractmethod
    def child(self, i):
        return 0

    @abc.abstractmethod
    def compare(self, x, y):
        return 0


class MinHeap(BinHeap):
    def __init__(self):
        super().__init__()

    def child(self, i):
        return self.minChild(i)

    def compare(self, x, y):
        return x < y

    def minChild(self, i):
        left = i * 2
        right = i * 2 + 1
        if right > self.size:
            return left

        if self.heap_list[left] < self.heap_list[right]:
            return left
        else:
            return right

    @staticmethod
    def heapfy(A):
        heap = MinHeap()
        heap.size = len(A)
        heap.heap_list = [0] + A
        i = len(A) // 2
        while i > 0:
            heap.bubbleDown(i)
            i -= 1

        return heap


class MaxHeap(BinHeap):
    def __init__(self):
        super().__init__()

    def child(self, i):
        return self.maxChild(i)

    def compare(self, x, y):
        return x > y

    def maxChild(self, i):
        left = i * 2
        right = i * 2 + 1
        if right > self.size:
            return left

        if self.heap_list[left] > self.heap_list[right]:
            return left
        else:
            return right

    @staticmethod
    def heapfy(A):
        heap = MaxHeap()
        heap.size = len(A)
        heap.heap_list = [0] + A
        i = len(A) // 2
        while i > 0:
            heap.bubbleDown(i)
            i -= 1

        return heap


print(MinHeap.heapfy([9, 6, 5, 2, 3]).heap_list)
print(MaxHeap.heapfy([9, 6, 5, 2, 3]).heap_list)
