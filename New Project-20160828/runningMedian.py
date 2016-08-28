from heapq import *

#Calculate median of a running stream of integers...

h = [1,7,10,12,13,14,9,6,4,17,3,18,20,24,28]
#max-heap on the left and min-heap on the right...
#1
#1;7
#1,7;10
#1,7;10,12
#1,7;10,12,13 -> 1,7,10; 12,13
#1,7,10;12,13,14

def rebalance(leftMaxHeap, rightMinHeap):
    if len(leftMaxHeap) > len(rightMinHeap) + 1:
        # 6, 4
        leftMax = -heappop(leftMaxHeap)
        heappush(rightMinHeap, leftMax)
    elif len(rightMinHeap) > len(leftMaxHeap):
        #4,5 or 4,6
        rightMin = heappop(rightMinHeap)
        heappush(leftMaxHeap, -rightMin)
    
    
leftMaxHeap = []
rightMinHeap = []
for num in h:
    if leftMaxHeap == []:
        heappush(leftMaxHeap, -num)
        continue
    leftMax = -heappop(leftMaxHeap)
    heappush(leftMaxHeap, -leftMax)
    rightMin = 999999999
    if rightMinHeap != []:
        rightMin = heappop(rightMinHeap)
        heappush(rightMinHeap, rightMin)
    
    if num >= rightMin:
        heappush(rightMinHeap, num)
    else:
        heappush(leftMaxHeap, -num)
    
    rebalance(leftMaxHeap, rightMinHeap)
    
    leftMax = -heappop(leftMaxHeap)
    heappush(leftMaxHeap, -leftMax)
    if rightMinHeap != []:
        rightMin = heappop(rightMinHeap)
        heappush(rightMinHeap, rightMin)
        
    print "Heaps: ", leftMaxHeap, "and ", rightMinHeap
    if len(leftMaxHeap) == len(rightMinHeap):
        print "Median =", (leftMax + rightMin)/2.0
    else:
        print "Median = ", leftMax        
    
