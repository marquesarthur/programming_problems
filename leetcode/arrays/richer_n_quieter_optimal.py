class Node:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.next = []
        self.checked = False
        self.is_root = True

    def add_edge(self, target):
        self.next.append(target)
        target.is_root = False


class Solution:
    def loudAndRich(self, richer, quiet):
        nodes = [Node(p, q) for p, q in enumerate(quiet)]

        for pair in richer:
            nodes[pair[1]].add_edge(nodes[pair[0]])

        [Solution.traverse(node) for node in nodes if node.is_root]

        return [node.p for node in nodes]

    @staticmethod
    def traverse(root):
        if root.checked:
            return

        root.checked = True

        if len(root.next) == 0:
            return

        for node in root.next:
            Solution.traverse(node)
            if node.q < root.q:
                root.q = node.q
                root.p = node.p




richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
# Output: [5,5,2,5,4,5,6,7]
print(Solution().loudAndRich(richer, quiet))



richer = [[0,1],[1,2]]
quiet = [1,0,2]
# Output: [5,5,2,5,4,5,6,7]
print(Solution().loudAndRich(richer, quiet))