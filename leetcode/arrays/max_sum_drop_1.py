class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        neg = [i for i, value in enumerate(arr) if value < 0]

        if len(neg) == len(arr):
            return min(arr)
        elif len(neg) == 1:
            arr.pop(neg[0])
            return sum(arr)
        else:
            i = 0
            result = 0
            # TODO: fix
            for j in neg:
                result = max(result, sum(arr[i:j]))
                i = j + 1

            result = max(result, sum(arr[i:len(arr)]))

            return result





#
# arr = [1,-2,0,3] # 4
# print(Solution().maximumSum(arr))
#
# arr = [1,-2,-2,3] # 3
# print(Solution().maximumSum(arr))

arr = [-1,-1,-1,-1] # 0
print(Solution().maximumSum(arr))


arr = [1,-4,-5,-2,5,0,-1,2]

print(Solution().maximumSum(arr))