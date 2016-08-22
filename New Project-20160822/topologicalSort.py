#Topological sorting..

from collections import defaultdict
class node():
    def __init__(self, val):
        self.val = val
        self.adjList = []
    
class Graph():
    def __init__(self):
        self.nodes = {}
        self.incoming = defaultdict(dict)
    
    def addEdge(self, v1, v2):
        if v1 not in self.nodes:
            self.nodes[v1] = node(v1)
        if v2 not in self.nodes:
            self.nodes[v2] = node(v2)
        
        n1 = self.nodes[v1]
        n2 = self.nodes[v2]
        if n2 not in n1.adjList:
            n1.adjList.append(n2)
    
    def printTopHelper(self, curNodeKey, stack, visited):
                
        for adjNode in self.nodes[curNodeKey].adjList:
            adjNodeKey = adjNode.val
            if adjNodeKey not in visited:
                if not self.printTopHelper(adjNodeKey, stack, visited):
                    return 0
        
        if curNodeKey in visited:           #Currently, this doesn't work....
            print "Tis not a DAG!!!"
            return 0
        visited[curNodeKey] = 1
          
        stack.append(self.nodes[curNodeKey].val)
        if len(stack) == len(self.nodes):
            print "Stack: ", stack[::-1]
        
        return 1       
    
    def printTopologicalSort(self):
        visited = {}
        stack = []
        for key in self.nodes.keys():
            if key not in visited:
                self.printTopHelper(key, stack, visited)

    def printAllTopHelper(self, key, stack, visited):
        #for adjNode in self.node[key].adjList:
        pass
        #Need to be completed...
            
    def printAllTopologicalSorts(self):
        visited = {}
        stack = []
        self.computeIncoming()
        for key in self.nodes.keys():
            if key not in self.incoming:
                self.printAllTopHelper(key, stack, visited)
        
    def computeIncoming(self):
        for nodeKey in self.nodes:
            for adjNode in self.nodes[nodeKey].adjList:
                adjNodeKey = adjNode.val
                self.incoming[adjNodeKey][nodeKey] = 1
            
if __name__ == "__main__":
    g = Graph()
    for tup in [(5,2), (2,3), (3,1), (5,0), (4,0), (4,1)]:
        g.addEdge(tup[0], tup[1])
    g.printTopologicalSort()
    g.computeIncoming()
    print g.incoming
    #g.printAllTopologicalSorts()
