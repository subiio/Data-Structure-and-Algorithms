class Node:
    def __init__(self, i, l=None):
        self.id = i
        self.link = l

    def __del__(self):
        if self.link is not None:
            del self.link

    def get_id(self):
        return self.id

    def get_link(self):
        return self.link

    def set_link(self, l):
        self.link = l


MAX_VTXS = 256

class AdjListGraph:
    def __init__(self):
        self.size = 0
        self.vertices = [None] * MAX_VTXS
        self.adj = [None] * MAX_VTXS

    def __del__(self):
        self.reset()

    def reset(self):
        for i in range(self.size):
            if self.adj[i] is not None:
                del self.adj[i]
        self.size = 0

    def is_full(self):
        return self.size >= MAX_VTXS

    def insert_vertex(self, val):
        if not self.is_full():
            self.vertices[self.size] = val
            self.adj[self.size] = None
            self.size += 1
        else:
            print("Error: 그래프 정점 개수 초과")

    def insert_edge(self, u, v):
        self.adj[u] = Node(v, self.adj[u])
        self.adj[v] = Node(u, self.adj[v])  # 방향 그래프의 경우 주석 처리

    def get_vertex(self, i):
        return self.vertices[i]

    def adjacent(self, v):
        return self.adj[v]

    def display(self):
        print(self.size)
        for i in range(self.size):
            print(f"{self.get_vertex(i)} ", end='')
            v = self.adj[i]
            while v is not None:
                print(f" {self.get_vertex(v.get_id())}", end='')
                v = v.get_link()
            print()


def main():
    g = AdjListGraph()
    
    for i in range(4):
        g.insert_vertex(chr(ord('A') + i))
    
    g.insert_edge(0, 1)
    g.insert_edge(0, 3)
    g.insert_edge(1, 2)
    g.insert_edge(1, 3)
    g.insert_edge(2, 3)
    
    print("인접 리스트로 표현한 그래프")
    g.display()

if __name__ == "__main__":
    main()



class Node:
    def __init__(self,id,l):
        self.id = id
        self.link = l
    def __del__(self):
        if not self.link is None:
            del self.link
    def get_id(self):
        return self.id
    def get_link(self):
        return self.link
    def set_link(self,l):
        self.link = l

class AdjListGraph:
    def __init__(self):
        self.size = 0
        self.vertices = [None] * MAX_VTXS
        self.adj = [None] * MAX_VTXS
    def __del__(self):
        self.reset()
    def reset(self):
        for i in range(self.size):
            if not self.adj[i] is None:
                del self.adj[i]
        
        self.size = 0
    def is_full(self):
        return self.size >= MAX_VTXS
    def insert_vertex(self,name):
        if not self.is_full():
            self.vertices[self.size] = name
            self.size += 1
        else:
            print("Error")
    def insert_edge(self,u,v):
        self.adj[u] = Node(v,self.adj[u])
        self.adj[v] = Node(u,self.adj[v])
    def 