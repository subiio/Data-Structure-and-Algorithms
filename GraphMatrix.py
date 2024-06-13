MAX_VTXS = 256

class AdjMatGraph:
    def __init__(self):
        self.size = 0
        self.vertices = [None] * MAX_VTXS
        self.adj = [[0] * MAX_VTXS for _ in range(MAX_VTXS)]
    
    def reset(self):
        self.size = 0
        self.vertices = [None] * MAX_VTXS
        self.adj = [[0] * MAX_VTXS for _ in range(MAX_VTXS)]
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size >= MAX_VTXS
    
    def insert_vertex(self, name):
        if not self.is_full():
            self.vertices[self.size] = name
            self.size += 1
        else:
            print("Error: 그래프 정점 개수 초과")
    
    def insert_edge(self, u, v):
        self.set_edge(u, v, 1)
        self.set_edge(v, u, 1)
    
    def delete_edge(self, u, v):
        self.set_edge(u, v, 0)
        self.set_edge(v, u, 0)
    
    def set_edge(self, i, j, val):
        self.adj[i][j] = val
    
    def get_vertex(self, i):
        return self.vertices[i]
    
    def get_edge(self, i, j):
        return self.adj[i][j]
    
    def adjacent(self, v):
        return [i for i, is_edge in enumerate(self.adj[v]) if is_edge]
    
    def display(self, fp=None):
        if fp is None:
            fp = sys.stdout
        
        print(self.size, file=fp)
        for i in range(self.size):
            print(f"{self.get_vertex(i)} ", end='', file=fp)
            for j in range(self.size):
                print(f" {self.get_edge(i, j):3}", end='', file=fp)
            print(file=fp)

import sys

def main():
    g = AdjMatGraph()
    
    for i in range(4):
        g.insert_vertex(chr(ord('A') + i))
    
    g.insert_edge(0, 1)
    g.insert_edge(0, 3)
    g.insert_edge(1, 2)
    g.insert_edge(1, 3)
    g.insert_edge(2, 3)
    
    print("인접 행렬로 표현한 그래프")
    g.display()

if __name__ == "__main__":
    main()

MAX_VTXS = 256

class AdjMatGraph:
    def __init__(self):
        self.size = 0
        self.vertices = [None] * MAX_VTXS
        self.adj = [ [0] * MAX_VTXS for _ in range(MAX_VTXS)]
    def reset(self):
        self.size = 0
        self.vertices = [None] * MAX_VTXS
        self.adj = [ [0] * MAX_VTXS for _ in range(MAX_VTXS)]
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size >= MAX_VTXS
    def insert_vertex(self, name):
        if not self.is_full():
            self.vertices[self.size] = name
            self.size += 1
        else:
            print("error")
    def set_edge(self,u,v,val):
        self.adj[u][v] = val
    def insert_edge(self, u,v):
        self.set_edge(u,v,1)
        self.set_edge(v,u,1)
    def delete_edge(self,u,v):
        self.set_edge(u,v,0)
        self.set_edge(v,u,0)
    def get_vertex(self,i):
        return self.vertices[i]
    def get_edge(self,u,v):
        return self.adj[u][v]
    def adjacent(self,v):
        return [i for i, is_edge in enumerate(self.adj[v]) if is_edge]


class AdjMatGraph:
    def __init__(self):
        self.size= 0 
        self.vertices = [None] * MAX_VTXS
        self.adj = [[0] * MAX_VTXS for _ in range(MAX_VTXS)]
    def reset(self):
        self.size= 0 
        self.vertices = [None] * MAX_VTXS
        self.adj = [[0] * MAX_VTXS for _ in range(MAX_VTXS)]
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size >= MAX_VTXS
    def insert_vertex(self,size,name):
        if not self.is_full():
            self.vertices[self.size] = name
            self.size += 1
        else:
            print("Error")
    def set_edge(self,u,v,val):
        self.adj[u][v] = val
    def insert_edge(self,u,v):
        self.set_edge(u,v,1)
        self.set_edge(v,u,1)
    def delete_edge(self,u,v):
        self.set_edge(u,v,0)
        self.set_edge(v,u,0)
    def 
    