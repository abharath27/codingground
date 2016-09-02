class IterDemo():
    def __init__(self):
        self.List = [1,2,3,4,5]
        self.indexToReturn = -1
        
    def __iter__(self):
        return self
        
    def next(self):
        self.indexToReturn += 1
        if self.indexToReturn == len(self.List):
            raise StopIteration
        return self.List[self.indexToReturn]
        

t = IterDemo()
print t.next()
print t.next()
print t.next()
