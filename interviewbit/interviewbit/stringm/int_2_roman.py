from bisect import bisect_right as upper_bound


class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        int_2_roman = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        nums = sorted(list(int_2_roman.keys()))

        solution = ""
        while A > 0:
            idx = upper_bound(nums, A)
            closest_2_A = nums[idx - 1]

            solution += int_2_roman[closest_2_A]
            A -= closest_2_A

        return solution
