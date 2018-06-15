class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        
        m = X[0]
    	n = Y[0]
    
    	totalJumps = 0
    
    	for i in xrange(len(X) - 1):
    
    		#print "from (%s %s) to (%s %s)" %(X[i], Y[i], X[i + 1], Y[i + 1])
    
    		currentX = X[i]
    		currentY = Y[i]
    
    		nextX = X[i + 1]
    		nextY = Y[i + 1]
    
    		# jumps from p1 to p2
    
    		xJumps = abs(currentX - nextX)
    		yJumps = abs(currentY - nextY)
    
    
    		# print "\n >>>> %s %s \n" %(xJumps, yJumps)
    		totalJumps += max(xJumps, yJumps)

        return totalJumps