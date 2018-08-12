class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):

        # 1st split by /
        # 2nd walk from left to right append "/" + value
        #   if "." skip
        #   if ".." pop last
        # epty stack concatenating results
        # O(n)


        # /a/./b/../../c/
        paths = A.split("/")  # ["", "a", ".", "b", "..", "..", "c", ""]
        stack = []
        for val in paths:
            if val == "":
                continue
            elif val == ".":
                continue
            elif val == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append("/" + val)
                # i = 1 [/a]
                # i = 2 [/a]
                # i = 3 [/a/b]
                # i = 4 [/a]
                # i = 5 []
                # i = 6 [/c]

        if not stack:
            return "/"

        result = ""
        while len(stack) > 0:
            result = stack.pop() + result

        return result
