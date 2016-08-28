from collections import defaultdict

#Freakin' finally. Implemented Trie..

class node():
    def __init__(self, eowMarker= 0, position=-1):
        self.eowMarker = eowMarker
        self.position = position                
        self.adjNodes = {}
    
class Trie():
    def __init__(self):
        self.head = node()
        
    def addWordHelper(self, word, root, pos):
        if word == "":
            return
        
        if word[0] in root.adjNodes:
            if len(word) == 1:
                root.adjNodes[word[0]].eowMarker = 1        #EOW Marker
                root.adjNodes[word[0]].position = pos
        else:
            if len(word) == 1:
                root.adjNodes[word[0]] = node(1, pos)
            else:
                root.adjNodes[word[0]] = node()
            
        self.addWordHelper(word[1:], root.adjNodes[word[0]], pos)
        
    def findWordHelper(self, word, root):
        if word == "":
            if root == None:
                return -1
            if root.eowMarker != 1:
                return -1
            return root.position
                
        if word[0] not in root.adjNodes:
            return -1
        if len(word) == 1 and root.adjNodes[word[0]].eowMarker != 1:
            return -1
        return self.findWordHelper(word[1:], root.adjNodes[word[0]])
            
    def addWord(self, word, pos):
        #Add a word to the trie..
        self.addWordHelper(word, self.head, pos)
        
    def findWord(self, word):
        #Find the position of the word in Trie..
        return self.findWordHelper(word, self.head)
    
    def printTrieHelper(self, root, prefix):
        if root == None:
            return
        for key in root.adjNodes:
            if root.adjNodes[key].eowMarker == 1:
                print prefix + key
                
            self.printTrieHelper(root.adjNodes[key], prefix + key)
    
    def printTrie(self):
        #Print all words in the trie
        self.printTrieHelper(self.head, "")
        
    
if __name__ == "__main__":
    t = Trie()
    for pos,word in enumerate(['abc','abcd','adc','aeb','aec','hello','hey','what','lol','hannah','hann']):
        t.addWord(word,pos)
        
   #t.printTrie()
    for word in ['abc','lol','hannah','what','hann','abcd','adc']:
        print t.findWord(word)
