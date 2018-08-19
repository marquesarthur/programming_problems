class Edge(object):
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight


class Vertex(object):
    def __init__(self, value, edges=[]):
        self.value = value
        self.edges = edges


def DFS(current, target, visited=set()):
    print("Visiting {}".format(current.value))
    if current == target:
        return True

    visited.add(current)
    result = False

    for e in current.edges:
        if e.to not in visited:
            result = result or DFS(e.to, target, visited)

    return result


a, b, c, d, e, f = Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"), Vertex("F")

# Directed graph
a.edges = [Edge(b, 9), Edge(c, 4)]
b.edges = [Edge(d, 12), Edge(e, 5)]
c.edges = [Edge(b, 4), Edge(e, 13)]
d.edges = [Edge(f, 2)]
e.edges = [Edge(f, 15)]

print("Searching for path A --> .. --> F")
print(DFS(a, f))
