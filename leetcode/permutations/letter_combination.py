
class Solution(object):
    """
    Time complexity : O(3^n x 4^m)
    where
        N is the number of digits in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8)
        M is the number of digits in the input that maps to 4 letters (e.g. 7, 9),
     and N+M is the total number digits in the input.

    O(3^n x 4^m): since one as to keep O(3^n x 4^m) solutions
    """

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': [' ']
        }
        result = []
        for i in range(len(digits)):
            current_digit = digits[i]

            if not result and current_digit in digit_to_letters:
                result = digit_to_letters[current_digit]

            elif current_digit in digit_to_letters:
                new_result = []

                for r in result:

                    aux = "".join(r)

                    for letter in digit_to_letters[current_digit]:
                        new_result.append(aux + letter)


                result = list(new_result)

        return result







digits = "23"
print(Solution().letterCombinations(digits))