class Solution(object):
    """
    Algorithm

    1. Initialize a stack S.
    2. Process each bracket of the expression one at a time.
    3. If we encounter an opening bracket, we simply push it onto the stack. This means we will process it later, let us simply move onto the sub-expression ahead.
    4. If we encounter a closing bracket, then we check the element on top of the stack. If the element at the top of the stack is an opening bracket of the same type, then we pop it off the stack and continue processing. Else, this implies an invalid expression.
    5. In the end, if we are left with a stack still having elements, then this implies an invalid expression.

    """


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        valid = ['(', ')', '{', '}', '[', ']']
        open_parenthesis = ['(', '{', '[']

        stack = []
        for i in range(len(s)):
            if s[i] in valid:
                if s[i] in open_parenthesis:
                    stack.insert(0, s[i])
                elif s[i] == ')':
                    if not stack:
                        return False
                    elif stack.pop(0) != '(':
                        return False
                elif s[i] == '}':
                    if not stack:
                        return False
                    elif  stack.pop(0) != '{':
                        return False
                elif s[i] == ']':
                    if not stack:
                        return False
                    elif  stack.pop(0) != '[':
                        return False

        return len(stack) == 0


print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([)]"))
print(Solution().isValid("{[]}"))
print(Solution().isValid("{{{{{{"))
print(Solution().isValid("}}}}}}}"))

