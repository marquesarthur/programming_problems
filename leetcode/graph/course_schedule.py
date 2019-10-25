from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        all_courses = set()

        graph = defaultdict(set)
        for course, prereq in prerequisites:
            graph[course].add(prereq)
            all_courses.add(course)
            all_courses.add(prereq)

        for c in xrange(numCourses):
            if c not in graph:
                graph[c] = set()

        possible_courses = sorted(
            [(c, len(v)) for c, v in graph.items()], key=lambda k: (k[1], -k[0])
        )

        taken_courses = set()
        for c, _ in possible_courses:
            prereq = graph[c]
            missing_prereq = list(filter(lambda p: p not in taken_courses, prereq))
            if not missing_prereq:
                taken_courses.add(c)
                if len(taken_courses) == numCourses:
                    return True


        if len(taken_courses) == numCourses:
            return True

        return False






#
# numCourses = 1
# prerequisites = [[1,0]]
# print(Solution().canFinish(numCourses, prerequisites))
#
# numCourses = 2
# prerequisites = [[1,0],[0,1]]
# print(Solution().canFinish(numCourses, prerequisites))
#
#
# numCourses = 3
# prerequisites = [[1,0],[2,1]]
# print(Solution().canFinish(numCourses, prerequisites))
#
#
# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# print(Solution().canFinish(numCourses, prerequisites))

numCourses = 8
prerequisites = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
print(Solution().canFinish(numCourses, prerequisites))