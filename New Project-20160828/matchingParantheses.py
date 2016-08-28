testStr = "[(((}{)))]"

#Test Matching parantheses
def isValid(testStr):
    stack = []
    for char in testStr:a
        if char in '[({':
            stack.append(char)
        elif char in ']})':
            if stack == []:
                print 'b'
                return 0
            matchingChar = stack.pop()
            if (matchingChar,char) not in [('(',')'), ('[',']'), ('{','}')]:
                print 'hey:', char, matchingChar
                return 0
    
    if stack != []:
        print 'c'
        return 0
    return 1
    
print isValid(testStr)
