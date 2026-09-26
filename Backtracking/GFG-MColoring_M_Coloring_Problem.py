class Solution :
    def m_coloring(self,v,edges,m):
        colors = []*v
        adj =[[] for i in range(v)]
        for u,w in edges:
            adj[u].append(w)
            adj[w].append(u)
        def is_safe(vertex,color,colors,adj):
            for neighbour in adj(vertex):
                if colors[neighbour] == color:
                    return False
            return True
        def solve(vertex,m,colors,adj):
            if vertex == v:
                return True
            for color in range(1,m+1):
                if not is_safe(vertex,color,colors,adj):
                    continue
                colors[vertex] == color
                if solve(vertex+1,m,colors,adj):
                    return True
                colors[vertex] == 0
            return False
        return solve(0,m,colors,adj)

