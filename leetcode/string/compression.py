class Solution(object):
    """
        This question is ambiguous. It does not state that counts >= 10 should take more than one space in the chars[]
        Technically, my solution works.
    """

    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) <= 1:
            return 1

        chars.sort()

        i = 0
        current_c = chars[i]
        current_sum = 1
        total = 0
        for j in range(1, len(chars)):
            if chars[j] == current_c:
                current_sum += 1
            elif current_sum > 1:
                chars[i] = current_c
                chars[i + 1] = str(current_sum)
                total += 1
                if i + 2 < len(chars):
                    chars[i + 2] = chars[j]

                current_c = chars[j]
                current_sum = 1
                i = i + 2
                total += 2
            else:
                total += 1
                current_c = chars[j]
                i += 1


            if j == len(chars) - 1 and current_sum > 1:
                chars[i] = current_c
                chars[i + 1] = str(current_sum)

        return total




    def compress_optimal(self, chars):
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1): # this affects the complexity. This is not O(n)
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write





#

input = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
s = Solution().compress_optimal(input)
print(input[:s])
#
# #
# input = ["a","a","b","b","c","c","c"]
# s = Solution().compress_optimal(input)
# print(input[:s])
# #
# #
# input = ["a"]
# s = Solution().compress_optimal(input)
# print(input[:s])
#
# input = ["a", "b"]
# s = Solution().compress_optimal(input)
# print(input[:s])
#
# input = ["a", "b", "c", "c"]
# s = Solution().compress_optimal(input)
# print(input[:s])
#
#
# input = ["a", "b", "c", "c", "a"]
# s = Solution().compress(input)
# print(input[:s])