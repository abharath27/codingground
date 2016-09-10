import copy
def nextPalin(num):
    num2 = list(str(num))
    mid = len(num2)/2
    n = len(num2)
    inc = 0
    incMid = 0

    for i in range(0,mid):
        if num2[n-i-1] < num2[i]:
            inc = 1
            num2[n-i-1] = num2[i]
        if num2[n-i-1] > num2[i] and inc != 1:
            incMid = 1
            break
        
    
    if incMid == 1 or inc != 1:
        if len(num2) % 2 == 1:
            l = int(''.join(num2[:(mid+1)])) + 1
            newNum = str(l) + str(l)[:-1][::-1]
            
        else:
            print 'num2 = ', num2
            l = int(''.join(num2[:mid])) + 1
            print 'l = ', l
            newNum = str(l) + str(l)[::-1]
        return ''.join(newNum) 
    
    return ''.join(num2)
      
n = input()
for i in range(n):
    print nextPalin(input())
            
