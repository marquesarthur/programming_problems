# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def overlapWith(self, other):
    	if other.start >= self.start and other.start <= self.end:
    		return True
    	else:
    		return False

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def getKey(self, interval):
    	return interval.start

    def merge(self, intervals):

    	if not intervals:
    		return []

    	partial = sorted(intervals, key = self.getKey)
    	result = []

    	# for x in partial:
    	# 	print "%s, %s" %(x.start, x.end)

    	i = 0
    	while i < len(partial):
    		# print "[%s, %s]" %(partial[i].start, partial[i].end)

    		current = partial[i]

    		j = i + 1
    		while j < len(partial):
    			next = partial[j]
    			if current.overlapWith(next):
    				if current.end > next.end:
    					current = Interval(current.start, current.end)
    				else:
    					current = Interval(current.start, next.end)
    				i += 1
    			else:
    				break
    			j += 1


    		result.append(Interval(current.start, current.end))
    		i += 1

    	# print "Teste"
    	# for x in result:
    	# 	print "%s, %s" %(x.start, x.end)

    	# print result

    	return result
    		
    			




assert(Solution().merge([Interval(1, 10), Interval(2, 9), Interval(3, 8), Interval(4, 7), Interval(5, 6), Interval(6, 6)]) == [Interval(1, 10)])

#assert(Solution().merge([[8,10],[15,18], [1,3],[2,6]]) == [[1, 6], [8, 10], [15, 18]])

