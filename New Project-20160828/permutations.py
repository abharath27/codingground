def getPermutations(l):
    if len(l) == 0:
        return ['']
    results = []
    swapped = {}
    for i in range(len(l)):
        if (l[0],l[i]) in swapped:
            continue
        swapped[(l[0],l[i])] = 1
        l[0], l[i] = l[i], l[0]
        results += [l[0] + perm for perm in getPermutations(l[1:])]
        l[i],l[0] = l[0], l[i]
    return results
    
print getPermutations(['1','1','2','1'])
