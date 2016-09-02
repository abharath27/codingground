class node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BST():
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        return BSTIterator(self)      #Creating an iterator class
        
    def _insertValHelper(self, root, val):
        if root == None:
            root = node(val)
        else:
            if val < root.val:
                root.left = self._insertValHelper(root.left, val)
            else:
                root.right = self._insertValHelper(root.right, val)
        return root
        
    def _printInOrderHelper(self, root):
        if root == None:
            return
        self._printInOrderHelper(root.left)
        print root.val
        self._printInOrderHelper(root.right)
        
    def insertVal(self, val):
        self.head = self._insertValHelper(self.head, val)
        
    def printInOrder(self):
        self._printInOrderHelper(self.head)

class BSTIterator():
    def __init__(self, bst):
        self.bst = bst
        self.stack = [(self.bst.head, 0)]
    
    def __nextHelper(self):
        if self.stack == []:
            raise StopIteration
        
        #print [x.val for x in self.stack]
        
        node, childrenPushed = self.stack.pop()
        if (node.left == None and node.right == None) or childrenPushed:
            return node.val
        else:
            if node.right != None:
                self.stack.append((node.right,0))
            self.stack.append((node,1))
            
            if node.left != None:
                self.stack.append((node.left,0))
        return self.__nextHelper()
    
    def next(self):
        #Do an inorder traversal.. Use a stack
        return self.__nextHelper()
        
        
if __name__ == "__main__":
    b = BST()
    for i in [5,4,9,2,3,1,8,10]:
        b.insertVal(i)
    #b.printInOrder()
    #bstIter = iter(b)
    #print bstIter.next()
    for val in b:
        print val
