class Solution:
    def __init__(self):
        self.graph = []
        self.weight = 0
        
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
        
    def find(self, parent, i):
        if parent[i-1] == i:
            return i
        parent[i-1] = Solution.find(self, parent, parent[i-1])
        return parent[i-1]
    
    def union(self, parent, rank, x, y):
        xroot = Solution.find(self, parent, x)
        yroot = Solution.find(self, parent, y)
        if rank[xroot-1] < rank[yroot-1]:
            parent[xroot-1] = yroot
        elif rank[xroot-1] > rank[yroot-1]:
            parent[yroot-1] = xroot
        else:
            parent[yroot-1] = xroot
            rank[yroot-1] += 1
        
    def solve(self, A, B):
        B = sorted(B, key = lambda x : x[2])
        l = len(B)
        parent = []
        rank = []
        edgesInGraph = 0
        for x in range(A):
            parent.append(x+1)
            rank.append(0)
        i = 0
        while edgesInGraph < A-1 and i<A:  
            u,v,w = B[i]
            i += 1
            x = Solution.find(self, parent, u)
            y = Solution.find(self, parent, v)
            if x != y:
                edgesInGraph += 1
                self.weight += w
                Solution.union(self, parent, rank, x, y)
        return self.weight
                    

