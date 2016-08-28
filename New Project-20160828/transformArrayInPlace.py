#http://www.ardendertat.com/2011/10/18/programming-interview-questions-9-convert-array/
#Transforming an array in place...

def getNewPos(i, n):
    return (i % (n/3))*3 + (i/ (n/3))
    
def rotate(a, orgI, n):
    i = getNewPos(orgI, len(a))
    temp = a[orgI]
    while 1:
        temp2 = a[i]
        a[i] = temp
        temp = temp2
        if i == orgI:
            break
        i = getNewPos(i, n)
  
def getCycleLength(i, n):
    visited = {}
    visited[i] = 1
    count = 1
    while 1:
        count += 1
        print i, getNewPos(i,n)
        i = getNewPos(i, n)
        if i in visited:
            #print visited
            #print 'i = ', i
            #print 'getNewPos = ', getNewPos(i,n)
            return count
        visited[i] = 1
            
def getCoverageFrom1And2(n):
    n1 = getCycleLength(1, n)
    n2 = getCycleLength(2, n)
    return n1 + n2
    
a = [0,3,6,9,1,4,7,10,2,5,8,11]
rotate(a, 1, len(a))
rotate(a, 2, len(a))
#print a
for i in range(20*3-1, 21*3-1, 3):
    getCoverageFrom1And2(i)
