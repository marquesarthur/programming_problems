# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.current = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.current < len(self.nums)


    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        val = self.nums[self.current]
        self.current += 1
        return val

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.queue = list()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """

        if self.queue:
            return self.queue[0]
        elif self.iterator.hasNext():
            value = self.iterator.next()
            self.queue.append(value)
            return self.queue[0]
        else:
            return None



    def next(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue.pop(0)
        else:
            return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return (self.queue and len(self.queue) > 0) or self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:

nums = [1, 2, 3]
iter = PeekingIterator(Iterator(nums))
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    print(iter.next())         # Should return the same value as [val].


iter = PeekingIterator(Iterator(nums))
iter.peek()
iter.peek()
print(iter.next())
print(iter.next())
print(iter.next())