
class Graph:
    def __init__(self):
        self.g = {}
        
    def addNode(self,n):
        self.g[n] = []
    
    def addEdge(self,i,j):
        self.g[i].append(i)
        self.g[j].append(j)
        
    def removeNode(self,n):
        for k in self.g[n]:
            self.g[k].remove(n)
        del self.g[n]
    
    def getNeigh(self,n):
        return self.g[k]
    
    def getNodeList(self):    
        return self.g.keys()
    
    