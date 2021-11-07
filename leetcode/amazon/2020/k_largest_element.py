

class Solution(object):

    def __insert_in_stack(self, num, k, stack):

        if len(stack) >= k:
            _min = stack[0]
            if num < _min:
                return
            else:
                stack.pop(0)

        stack.append(num)
        stack.sort()
        return





    def k_largest(self, nums, k):
        # define aux array of length K
        # for nums[k+1: ] do:
        #   if nums[i] > max in k: pop mim and append nums[i]
        # return stack
        # assume k is always valid:

        stack = [] # min always on top of the stack

        for i in nums:
            self.__insert_in_stack(i, k, stack)


        return stack[0]







a = [1, 23, 12, 9, 30, 2, 50]
k = 3

print(Solution().k_largest(a, k))

# 50, 30 and 23.