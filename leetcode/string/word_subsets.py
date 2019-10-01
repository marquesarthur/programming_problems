class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        result = []

        all_leters = {}
        for word in B:
            all_b_letters = {}
            for c in word:
                if c not in all_b_letters:
                    all_b_letters[c] = 0

                all_b_letters[c] += 1

            for c, count in all_b_letters.items():
                if c not in all_leters:
                    all_leters[c] = count
                else:
                    all_leters[c] = max(count, all_leters[c])

        for word in A:
            all_a_letters = {}
            for c in word:
                if c not in all_a_letters:
                    all_a_letters[c] = 0

                all_a_letters[c] += 1

            is_subset = True
            for c, count in all_leters.items():
                if c not in all_a_letters:
                    is_subset = False
                    break
                elif all_a_letters[c] < count:
                    is_subset = False
                    break

            if is_subset:
                result.append(word)

        return result

#
A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","o"]
print(Solution().wordSubsets(A, B)) # ["facebook","google","leetcode"]

A = ["amazon","apple","facebook","google","leetcode"]
B = ["l","e"]
print(Solution().wordSubsets(A, B)) # ["apple","google","leetcode"]

A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","oo"]
print(Solution().wordSubsets(A, B)) # ["facebook","google"]

A = ["amazon","apple","facebook","google","leetcode"]
B = ["lo","eo"]
print(Solution().wordSubsets(A, B)) # ["google","leetcode"]

A = ["amazon","apple","facebook","google","leetcode"]
B = ["ec","oc","ceo"]
print(Solution().wordSubsets(A, B)) # ["facebook","leetcode"]