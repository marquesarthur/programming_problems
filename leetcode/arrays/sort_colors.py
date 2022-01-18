class Solution(object):


    def sort_color(self, nums, current_index, color):
        for i in range(current_index, len(nums)):
            if nums[i] == color:
                nums[current_index], nums[i] = nums[i], nums[current_index]
                current_index += 1

        return current_index

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # red, white, and blue
        idx_red = -1
        idx_white = -1
        idx_blue = -1

        RED = 0
        WHITE = 1
        BLUE = 2

        #  means I have all pointers to do what it needs to be done
        for i, value in enumerate(nums):
            if value == RED and idx_red == -1:
                idx_red = i
            if value == WHITE and idx_white == -1:
                idx_white = i
            if value == BLUE and idx_blue == -1:
                idx_blue = i

        current_idx = 0
        if idx_red != -1:
            current_idx = self.sort_color(nums, current_idx, RED)

        if idx_white != -1:
            current_idx = self.sort_color(nums, current_idx, WHITE)

        if idx_blue != -1:
            current_idx = self.sort_color(nums, current_idx, BLUE)



        


# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)