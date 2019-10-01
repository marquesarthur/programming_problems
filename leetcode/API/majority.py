from collections import Counter

class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.count_at_idx = {}


        for idx, number in enumerate(arr):
            if idx > 0:
                self.count_at_idx[idx] = dict(self.count_at_idx[idx - 1])
            else:
                self.count_at_idx[idx] = {}

            if number not in self.count_at_idx[idx]:
                self.count_at_idx[idx][number] = 0

            self.count_at_idx[idx][number] += 1


    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        if left > right:
            return -1

        if right >= len(self.count_at_idx.keys()):
            return - 1

        if threshold > (right - left) / 2:
            return -1


        left_idxs = {}
        if left > 0:
            left_idxs = self.count_at_idx[left - 1]

        upper_values = dict(self.count_at_idx[right])

        for number in upper_values.keys():
            current = upper_values[number]
            if number in left_idxs:
                current -= left_idxs[number]

            if current >= threshold:
                return number


        return -1



import collections
import bisect

class MajorityCheckerOptimal:
    """
        Make a map of numbers and the indexes that they appear in
        create a list of the numbers sorted in decreasing order by the amount of times that they appear in the map
    """

    def __init__(self, arr):
        self.loc = collections.defaultdict(list)
        for i, n in enumerate(arr):
            self.loc[n].append(i)
        self.nums = sorted(self.loc.keys(), key=lambda n: len(self.loc[n]), reverse=True)

    def query(self, left, right, threshold):
        """
            Iterate numbers. If the length of the indexes in the map at [number] is smaller than [t] return -1.
                This means no majority

            count num of indexes < left
            count num of indexes <= right
            subtract right and left
            if result > [t] return n

        :param left:
        :param right:
        :param threshold:
        :return:
        """
        for n in self.nums:
            aux = self.loc[n]
            if len(aux) < threshold: return -1

            l, r = bisect.bisect_left(aux, left), bisect.bisect_right(aux, right)
            if r - l >= threshold: return n
        return -1



majorityChecker =  MajorityCheckerOptimal([1,1,2,2,1,1])
print(majorityChecker.query(0,5,4)) # returns 1
print(majorityChecker.query(0,3,3)) # returns -1
print(majorityChecker.query(2,3,2)) # returns 2