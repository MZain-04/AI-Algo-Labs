#implementation of BFS


class Graph():

    def __init__(self):
        self.graph={}

    def add_edge(self,first,second):

        if first not in self.graph:
            self.graph[first] = []
      
        if second not in self.graph:
            self.graph[second] = []

        self.graph[first].append(second)
        self.graph[second].append(first)

    def bfs(self,start):
        queue=[]
        visited=[]

        #starting node in queue
        queue.append(start)

        # start node as visited node
        visited.append(start)

        while len(queue)>0:
            #removing first node from queue so that others can appear
            current=queue.pop(0)

            print(current,end=" ")

            #checking all neighbours
            for neighbour in self.graph[current]:
                if neighbour not in visited:
                    #putting neighbour in queue
                    queue.append(neighbour)

                    # mark neighbour as visited
                    visited.append(neighbour)


obj = Graph()
obj.add_edge(0,1)
obj.add_edge(0,4)
obj.add_edge(1,4)
obj.add_edge(1,3)
obj.add_edge(4,3)
obj.add_edge(1,2)
obj.add_edge(3,2)


print("BFS TRAVERSAL:")
obj.bfs(2)

    