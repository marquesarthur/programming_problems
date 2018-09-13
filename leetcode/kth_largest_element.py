# Method 2 (Using Min Heap – HeapSelect)
# We can find k’th smallest element in time complexity better than O(nLogn).
# A simple optomization is to create a Min Heap of the given n elements and call extractMin() k times.

import heapq


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        i = 0
        j = len(nums) - k
        while i < j:
            heapq.heappop(nums)
            i += 1

        return heapq.heappop(nums)

A = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(A, k))

A = [3,2,3,1,2,4,5,5,6]
k = 4
print(Solution().findKthLargest(A, k))