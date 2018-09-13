# Efficient Approach : Use bit manipulation in order to find the quotient. The divisor and dividend can be written as
#
# dividend = quotient * divisor + remainder
#
# As every number can be represented in base 2(0 or 1), represent the quotient in binary form by using shift operator as given below :
#
# Determine the most significant bit in the quotient. This can easily be calculated by iterating on the bit position i from 31 to 1.
# Find the first bit for which divisor << i is less than dividend and keep updating the ith bit position for which it is true.
# Add the result in temp variable for checking the next position such that (temp + (divisor << i) ) is less than dividend.
# Return the final answer of quotient after updating with corresponding sign.

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = -1 if ((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient, temp = 0, 0

        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                quotient |= (1 << i)
                temp += divisor << i

        result = sign * quotient
        if -2**31 <= result and result <= 2**31 -1:
            return result
        else:
            return 2**31 -1



print(Solution().divide(10, 3)) # 3
print(Solution().divide(-2147483648, -1))