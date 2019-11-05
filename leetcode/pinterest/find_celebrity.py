
import random
from collections import defaultdict

THEMSELVES = 1

class Solution(object):

    def __init__(self, graph):
        self.graph = graph


    def knows(self, a, b):
        if self.graph and self.graph[a][b] == 1:
            return True

        return False


    def findCelebrity(self, n):

        # greedy depth first search
        # while I did not talk to everyone do:
        # asks if A knows B
        # if answer is yes: put B on the stack and move to him
        # if answer is no: keep asking until you asked about everyone


        stack = []
        visited = set()

        for people in xrange(n):
            stack.append(people)



        # The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
        know_count = defaultdict(set)
        by_themselves = set()

        while len(visited) < n and stack:

            a = stack.pop()
            visited.add(a)

            kcount = 0
            for b in xrange(n):
                if self.knows(a, b):
                    kcount += 1
                    if a != b:
                        know_count[b].add(a)
                    if b not in visited:
                        stack.append(b)

            if kcount == THEMSELVES:
                by_themselves.add(a)


        for people in by_themselves:
            if people in know_count and len(know_count[people]) == n - 1:
                return people


        return -1







graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
] # 1

print(Solution(graph).findCelebrity(len(graph)))


graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
] #  -1
print(Solution(graph).findCelebrity(len(graph)))




graph = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0], # knows only himself but not celebrity
    [0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1]
] #  -1
print(Solution(graph).findCelebrity(len(graph)))


