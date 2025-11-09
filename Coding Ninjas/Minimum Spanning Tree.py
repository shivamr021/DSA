from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

# Edge class for storing the Edges of thee graph
class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

def findParent(v, parent):
    if parent[v] == v:
        return v
    parent[v] = findParent(parent[v], parent)
    return parent[v]

def union(v1, v2, parent, rank):
    p1 = findParent(v1, parent)
    p2 = findParent(v2, parent)
    if p1 != p2:
        if rank[p1] < rank[p2]:
            parent[p1] = p2
        elif rank[p1] > rank[p2]:
            parent[p2] = p1
        else:
            parent[p2] = p1
            rank[p1] += 1

def minimumSpanningTree(edges, V, E):
    edges.sort(key=lambda edge: edge.weight)
    parent = [i for i in range(V)]
    rank = [0 for _ in range(V)]
    
    mst_weight = 0
    edges_used = 0
    
    for edge in edges:
        if edges_used == V - 1:
            break
        p1 = findParent(edge.start, parent)
        p2 = findParent(edge.end, parent)
        
        if p1 != p2:
            union(p1, p2, parent, rank)
            mst_weight += edge.weight
            edges_used += 1
    
    return mst_weight

#taking inpit using fast I/O
def takeInput():
    n_m = stdin.readline().strip().split(" ")
    V = int(n_m[0].strip())
    E = int(n_m[1].strip())

    edges = [Edge(0, 0, 0) for i in range(E)]
    for i in range(E):
        temp = list(map(int, stdin.readline().strip().split(" ")))
        edges[i] = Edge(temp[0], temp[1], temp[2])
    return edges, V, E

#main
edges, V, E = takeInput()
print(minimumSpanningTree(edges, V, E))
