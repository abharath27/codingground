#Trie implementation

class node():
    def __init__(self, stopper = False):
        self.stopper = stopper
        self.children = {}

class Trie():
    def __init__(self):
        self.root = node()
        pass
    
    
    def addWord(self, word):
        curNode = self.root
        for i in range(len(word)):
            if word[i] not in curNode.children:
                curNode.children[word[i]] = node(i == len(word)-1)
            else:
                if i == len(word)-1:
                    curNode.children[word[i]].stopper = True
            curNode = curNode.children[word[i]]
    
    def search(self, subStr):
        curNode = self.root
        flag = 1
        for i in range(len(subStr)):
            if subStr[i] not in curNode.children:
                flag = 0
                break
            curNode = curNode.children[subStr[i]]
        return self.getAllWordsUnderRoot(curNode, subStr)
        
    def getAllWordsUnderRoot(self, root, prefix):
        if root.children == {}:
            return [""]
        resultSet = []
        for child in root.children:
            print 'child: ', child, 'prefix:', prefix
            for eachChildString in self.getAllWordsUnderRoot(root.children[child], prefix + child):
                resultSet += [prefix + child + eachChildString]
        
        print 'resultSet:', resultSet
        return resultSet
        
    def printTrieHelper(self, root):
        if root == None:
            return
        print 
        for child in root.children:
            print child,
        print
        for child in root.children:
            self.printTrieHelper(root.children[child])
            
    def printTrie(self):
        self.printTrieHelper(self.root)
        
if __name__ == "__main__":
    t = Trie()
    for word in ['ha','hb']:
        t.addWord(word)
     
    #t.printTrie()   
    print t.getAllWordsUnderRoot(t.root, "h")