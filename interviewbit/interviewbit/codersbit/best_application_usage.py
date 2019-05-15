from bisect import bisect_right as upper_bound
#
#
# def insert(current, currentBack, stack):
#     total = current[1] + currentBack[1]
#     while len(stack) > 0 and stack[len(stack) - 1][2] < total:
#         stack = stack[:len(stack) - 1]
#
#     if len(stack) == 0:
#         stack.append((
#             current,
#             currentBack,
#             current[1] + currentBack[1]
#         ))
#     elif stack[len(stack) - 1][2] <= total:
#         stack.append((
#             current,
#             currentBack,
#             current[1] + currentBack[1]
#         ))
#
#
# class Solution:
#     def solve(self, forward, backward, N):
#         forward = sorted(forward, key=lambda k: k[1])
#         backward = sorted(backward, key=lambda k: k[1])
#
#         i = len(forward) - 1
#
#         stack = []
#         solution = []
#
#         while (i >= 0):
#             current = forward[i]
#
#             currentTarget = N - current[1]
#
#             values = upper_bound([i[1] for i in backward], currentTarget)
#
#             if values > 0:
#                 j = values - 1
#                 while j >= 0 and currentTarget >= 0:
#                     currentBack = backward[j]
#                     if stack and stack[len(stack) - 1][2] > current[1] + currentBack[1]:
#                         break
#                     if currentBack[1] <= currentTarget:
#                         insert(current, currentBack, stack)
#                     j -= 1
#
#             i -= 1
#
#         for s in stack:
#             solution.append([s[0][0], s[1][0]])
#
#         return sorted(solution, key=lambda k: (k[0], k[1]))
#
#
#
#
#



def optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList):
    pairs = []

    if deviceCapacity <= 0:
        return pairs

    foregroundAppList = sorted(foregroundAppList, key=lambda k: k[1])
    backgroundAppList = sorted(backgroundAppList, key=lambda k: k[1])

    i = len(foregroundAppList) - 1
    stack = []
    while (i >= 0):
        foregroundApp = foregroundAppList[i]
        id = foregroundApp[0]
        memory = foregroundApp[1]

        target = deviceCapacity - memory
        values = upper_bound([k[1] for k in backgroundAppList], target)

        if values > 0:
            for j in xrange(values - 1, -1, -1):
                id_back = backgroundAppList[j][0]
                memory_back = backgroundAppList[j][1]

                if memory + memory_back <= deviceCapacity:

                    if not stack:
                        stack.append([id, id_back, memory + memory_back])
                    elif stack[-1][2] == memory + memory_back:
                        stack.append([id, id_back, memory + memory_back])

        i -= 1

    for s in stack:
        pairs.append([s[0], s[1]])

    return sorted(pairs, key=lambda k: (k[0], k[1]))



deviceCapacity = 20
foregroundAppList = [[1, 8], [2, 7], [ 3, 14]]
backgroundAppList = [[1, 5], [2, 10], [3, 14]]

print(optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList))