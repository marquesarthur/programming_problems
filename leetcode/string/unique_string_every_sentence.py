class Solution():

    def uniqueIn(self, s):

        map_word_indexes = {}
        for idx, sentence in enumerate(s):
            for word in sentence.split(' '):
                if word not in map_word_indexes:
                    map_word_indexes[word] = set()

                map_word_indexes[word].add(idx)

        result = []
        for idx, sentence in enumerate(s):
            for word in sentence.split(' '):
                if len(map_word_indexes[word]) == 1 and word not in result:
                    result.append(word)

        return result





s = [
"My dog eats food",
"She eats food too",
"My dog food is good good"
]

expected = ['She', 'too', 'is', 'good']
print(Solution().uniqueIn(s))