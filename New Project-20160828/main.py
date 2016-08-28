import math

def recursivePermutations(string):
    if string == "":
        return [""]
    perms = recursivePermutations(string[1:])
    
    resultList = []
    positionList = {}
    for perm in perms:
        for i,eachChar in enumerate(perm):
            if eachChar == string[0]:
                positionList[i] = 1
        
        for i in range(len(string)):
            if i-1 not in positionList:
                resultList.append(perm[:i] + string[0] + perm[i:])
    
    return resultList
            
#Iterative algo to generate nth permutation in a string with no characters repeated..

def getPermutation(string, n):
    resultStr = ""
    if string == "":
        return ""
    while string !="":
        pos = n / math.factorial(len(string)-1)
        resultStr = resultStr + string[pos] 
        n = n % math.factorial(len(string)-1)
        string = string[:pos] + string[pos+1:]
    return resultStr

#Iterative algo to generate nth permutation in a string with repeating characters

#aaab
#aab -> aaab, aaba
#aba -> aaba, abaa
def getPermutation(string, n):
    resultStr = ""
    if string == "":
        return ""
    while string !="":
        pos = n / math.factorial(len(string)-1)
        resultStr = resultStr + string[pos] 
        n = n % math.factorial(len(string)-1)
        string = string[:pos] + string[pos+1:]
    return resultStr



    
str1 = 'aab'
print sorted(recursivePermutations(str1))
#for i in range(math.factorial(len(str1))):
    #print getPermutation(str1, i)
