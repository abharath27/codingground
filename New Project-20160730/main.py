#Given a random string S and another string T with unique elements, find the minimum consecutive sub-string of S such that it contains all the elements in T. 
#example: 
#S='adobecodebanc' 
#T='abc' 
#answer='banc'
from collections import OrderedDict

s = "adobecodebanchellothereaadsbcalskjd;fas"
t = "abc"

d = OrderedDict()
windowStart = -1
windowEnd = -1
windowSize = -1

for i in range(len(s)):
    if s[i] in t:
        if s[i] in d:
            del d[s[i]]
        d[s[i]] = i
        print d
        if len(d) == len(t):
            tempStart = next(iter(d.values()))
            tempEnd = next(reversed(d.values()))
            #print windowStart
            #print windowEnd
            if windowSize == -1 or windowSize > (tempEnd - tempStart):
                windowSize = tempEnd - tempStart
                windowStart = tempStart
                windowEnd = tempEnd
            print [windowSize, windowStart, windowEnd]
    
print s[windowStart:windowEnd+1]    
