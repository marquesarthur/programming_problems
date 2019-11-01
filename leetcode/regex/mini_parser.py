# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """
       self._int = None
       self._elements = None
       if value:
           self.setInteger(value)
       else:
           self._elements = []


   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if "," in s:
            head = NestedInteger(value=int(s[1:s.index(",")]))
            tail = Solution().deserialize(s[s.index(",") + 1:len(s) - 1])
            result = NestedInteger()
            result.add(head)
            result.add(tail)
            return result
        else:
            return NestedInteger(value=int(s.replace("[", "").replace("]", "")))





# Given
s = "324"
Solution().deserialize(s)

# You should return a NestedInteger object which contains a single integer 324.

# Given
s = "[123,[456,[789]]]"
Solution().deserialize(s)

# Return a NestedInteger object containing a nested list with 2 elements:
#
# 1. An integer containing value 123.
# 2. A nested list containing two elements:
#     i.  An integer containing value 456.
#     ii. A nested list with one element:
#          a. An integer containing value 789.