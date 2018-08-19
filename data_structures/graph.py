class Edge(object):
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight


class Vertex(object):
    def __init__(self, value, edges=[]):
        self.value = value
        self.edges = edges


class Graph(object):
    def __init__(self, vertexes):
        self.vertexes = vertexes


a, b, c, d, e, f = Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"), Vertex("F")

# Undirected graph
a.edges = [Edge(b, 9), Edge(c, 4)]
b.edges = [Edge(d, 12), Edge(e, 5), Edge(a, 9), Edge(c, 4)]
c.edges = [Edge(b, 4), Edge(e, 13), Edge(a, 4)]
d.edges = [Edge(f, 2), Edge(b, 12), Edge(e, 3)]
e.edges = [Edge(f, 15), Edge(d, 3), Edge(c, 13), Edge(b, 5)]
f.edges = [Edge(d, 2), Edge(e, 15)]


# Directed graph
# a.edges = [Edge(b, 9), Edge(c, 4)]
# b.edges = [Edge(d, 12), Edge(e, 5)]
# c.edges = [Edge(b, 4), Edge(e, 13)]
# d.edges = [Edge(f, 2)]
# e.edges = [Edge(f, 15)]


g = Graph([a, b, c, d, e, f])