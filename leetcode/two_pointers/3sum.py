class Solution(object):

        def threeSum(self, nums):

            A = sorted(nums)
            n = len(A)

            result = set()

            for i in range(n):

                j = i + 1
                k = n - 1

                target = A[i]

                while j < k:
                    if target + A[j] + A[k] < 0:
                        j += 1
                    elif target + A[j] + A[k] > 0:
                        k -= 1
                    else:
                        result.add((A[i], A[j], A[k]))
                        j += 1

            return sorted(list(result))



#
# class Solution(object):
#
#     def bin_search(self, nums, target, i, j):
#
#         if i > j:
#             return -1
#
#         mid = (i + j) / 2
#
#         if nums[mid] == target:
#             return mid
#
#         elif nums[mid] < target:
#             return self.bin_search(nums, target, mid + 1, j)
#         else:
#             return self.bin_search(nums, target, i, mid - 1)
#
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums = sorted(nums)
#         result = set()
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if i != j:
#
#                     target = -nums[i] + -nums[j]
#
#                     k = self.bin_search(nums, target, 0, len(nums) - 1)
#
#                     if k != -1 and k != i and k != j:
#                         aux = sorted([nums[i], nums[j], nums[k]])
#                         result.add((aux[0], aux[1], aux[2]))
#
#
#         return [list(a) for a in result]





A = [-1, 0, 1, 2, -1, -4]


print(Solution().threeSum(A))