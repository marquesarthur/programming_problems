from collections import defaultdict

class Solution:
    
    def height_from(self, e, _edges):
        all_nodes = _edges.values()
        visited = []
        stack = []
        
        
        stack.append((e, 0))
        result = 0
        while stack and len(visited) < len(all_nodes):
            edge, distance = stack.pop()
            visited.append(edge)
            result = max(result, distance)
            for c in _edges[edge]:
                if c not in visited:
                    stack.append((c, distance + 1))
        
        
        
        return result
    
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        _edges = defaultdict(set)
        for i in edges:
            _from = i[0]
            _to = i[1]
            _edges[_from].add(_to)
            _edges[_to].add(_from)
            
            
        for i in range(n):
            if i not in _edges:
                _edges[i] = set()
            
        _min = n
        _height_node = defaultdict(list)
        
        # start by nodes with maximum number of edges
        
        with_most_leaves = sorted([(k, len(v)) for k, v in _edges.items()], key=lambda x: x[1], reverse=True)
        
        for w in with_most_leaves:
            e, leaves = w
            height = self.height_from(e, _edges)
            if height > _min:
                break
            _height_node[height].append(e)
            _min = min(_min, height)
            
        return _height_node[_min]
            

class SolutionOptimal:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

	G = [ [] for i in range(n) ]
	for (u,v) in edges: 
		G[u].append(v)
		G[v].append(u)

	nodes = list(range(len(G)))
	is_leaf = lambda u: len(G[u]) == 1
	leaves = { x for x in nodes if is_leaf(x) }

	count = 0
	while n - count > 2:
		new_leaves, count = set(), count + len(leaves)
		for u in leaves:
				v = G[u][0]
				G[v].remove(u)
				G[u].clear()
				if is_leaf(v): new_leaves.add(v)
		leaves = new_leaves

	return leaves        
