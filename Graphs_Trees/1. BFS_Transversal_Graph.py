from collections import defaultdict,deque

class Graph:
    def __init__(self, n):
        self.ajdlist = defaultdict(list)
        self.maxKeys = n
    def addEdge(self, u, v):
        self.ajdlist[u].append(v)
    def bfs_Trans(self, startNode):
        #queue=[] 
        queue = deque()
        visited = [False]*(self.maxKeys) #since this bfs is for graph so it can be cyclic hence we use visited to check if the node was visited before or not.
        
        visited[startNode]=True
        queue.append(startNode)
        
        while(queue):
            #currentNode = queue.pop()
            currentNode = queue.popleft() #this is when you use deque
            print(currentNode, end = ' ')
            
            for neighbor in self.ajdlist[currentNode]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
graph = Graph(5) #creating graph
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 4)
print("BFS Transversal from root:")
graph.bfs_Trans(0)
