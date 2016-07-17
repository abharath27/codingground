#Implementing LRU cache in python
import collections

class LRUCache:
    def __init__(self, size):
        self.cacheSize = size
        self.cache = collections.OrderedDict()
        self.numFaults = 0
    
    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except:
            return -1
            
    def set(self, key, value):
        self.numFaults += 1
        if  key in self.cache:
            del self.cache[key]
            self.numFaults -= 1
        elif len(self.cache) == self.cacheSize:
            self.cache.popitem(last = False)
        self.cache[key] = value

cache = LRUCache(2)
#a = [(1,'a'),(2,'b'),(1,'c'),(5,'e'),(1,'f'),(4,'d')]
#for item in a:
#    cache.set(item[0], item[1])
#    print cache.cache
raw_input()
inputList = map(int, raw_input().split()[1:])            
for item in inputList:
    cache.set(item,"")
    #print cache.cache
    #print 'faults =', cache.numFaults
print cache.numFaults