# from collections import defaultdict
#
# class Solution(object):
#
#     def next_positions(self, N, r, c):
#         moves = []
#         if r - 2 >= 0:
#             if c - 1 >= 0:
#                 moves.append((r - 2, c - 1))
#             if c + 1 < N:
#                 moves.append((r - 2, c + 1))
#
#         if r - 1 >= 0:
#             if c - 2 >= 0:
#                 moves.append((r - 1, c - 2))
#             if c + 2 < N:
#                 moves.append((r - 1, c + 2))
#
#         if r + 1 < N:
#             if c - 2 >= 0:
#                 moves.append((r + 1, c - 2))
#             if c + 2 < N:
#                 moves.append((r + 1, c + 2))
#
#         if r + 2 < N:
#             if c - 1 >= 0:
#                 moves.append((r + 2, c - 1))
#             if c + 1 < N:
#                 moves.append((r + 2, c + 1))
#
#         return moves
#
#     def move(self, chess, N, K, r, c, probs):
#         if K <= 0:
#             return
#
#         next_positions = self.next_positions(N, r, c)
#
#         for r_next, c_next in next_positions:
#             if not chess[r_next][c_next]:
#                 probs[K] += 1
#                 self.move(chess, N, K - 1, r_next, c_next, probs)
#             else:
#                 probs[K] += probs[K-1]
#                 self.move(chess, N, K - 1, r_next, c_next, probs)
#
#     def knightProbability(self, N, K, r, c):
#         """
#         :type N: int
#         :type K: int
#         :type r: int
#         :type c: int
#         :rtype: float
#         """
#         if K == 0:
#             return 1.
#
#         chess = [[False for _ in xrange(N)] for _ in xrange(N)]
#         probs = defaultdict(int)
#         probs[(r, c)] = 1
#         self.move(chess, N, K, r, c, probs)
#
#         p = sum(probs.values()) / float(8**K)
#
#
#         return p

class Solution:
    def knightProbability(self, N, K, r, c):
        if (K == 0):
            return (1)

        moves = [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]
        prev = {(r, c): 1.}

        curr = {}
        for __ in range(K):
            curr = {}
            for node in prev.keys():
                for (x, y) in moves:
                    x0, y0 = node[0] + x, node[1] + y
                    if (0 <= x0 < N and 0 <= y0 < N):
                        if ((x0, y0) in curr):
                            curr[(x0, y0)] += prev[node]
                        else:
                            curr[(x0, y0)] = prev[node]
            prev = curr

        return sum(curr.values()) / float(8**K)

#
N, K, r, c = 3, 2, 0, 0
print(Solution().knightProbability(N, K, r, c))


N, K, r, c = 3, 3, 0, 0
print(Solution().knightProbability(N, K, r, c))