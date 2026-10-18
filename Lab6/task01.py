from collections import defaultdict


class Graph():

    def __init__(self,V):
        #number of vertices
        self.V=V

        #adjancy lists
        self.adj = defaultdict(list)

    def add_edge(self,v,w):
        # add w to v's list
        self.adj[v].append(w)

    def _dfs_util(self,v,visited):

        #mark the current node as visited and print it
        visited[v]= True
        print(v,end=" ")


        #Recur for all the vertices adjacent to this vertex
        for neighbour in self.adj[v]:
            if not visited[neighbour]:
                self._dfs_util(neighbour,visited)


    def dfs(self,v):

        #mark all the vertices as not visited
        visited = [False] * self.V

        #call the recursive helper function to print DFS traversal
        self._dfs_util(v,visited)

g= Graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)

print("Following is Depth First Traversal starting from vertex 2")
g.dfs(1)
