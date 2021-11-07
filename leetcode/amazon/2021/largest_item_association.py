from collections import defaultdict


def dfs(start, group, graph, visited):
    group.append(start)
    visited.add(start)
    for asso in graph[start]:
        if asso not in visited:
            dfs(asso, group, graph, visited)

def item_association(pairs):
    graph = defaultdict(list)
    for a, b in pairs: # building adjlist
        graph[a].append(b)
        graph[b].append(a)
        
    visited = set()
    res = []
    for k in graph.keys():
        if k not in visited:
            group = []
            dfs(k, group, graph, visited)
            if len(group) > len(res):
                res = group
    return res





def largest_association(item_set):
    # walk through each item
    # add item to dictionary

    all_items = defaultdict(set)

    for pair in item_set:

        a, b = pair[0], pair[1]

        all_items[a].add(a)
        all_items[a].add(b)

        all_items[b].add(a)
        all_items[b].add(b)

    result = sorted(all_items.values(), key=lambda k: len(k), reverse=True)

    partial = [result[0]]
    for i in range(1, len(result)):
        if len(result[i]) == len(result[0]):
            partial.append(result[i])
        else:
            break

    # sort list lexicographically

    result = sorted(partial, key= lambda k: ' '.join(k))[0]
    result = list(result)
    return result


# from definition, it will always be a pair
itemAssociation = [
    ["Item1", "Item2"],
    ["Item3", "Item4"],
    ["Item4", "Item5"]
]


# print(largest_association(itemAssociation))

print(item_association(itemAssociation))

# Output:
# [Item3, Item4, Item5]
