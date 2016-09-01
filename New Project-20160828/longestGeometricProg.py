#Finding the longest geometric progression in an array
def f(arr, i, dp):
    if i < 0:
        return
    if (i,1) in dp:
        return
    f(arr, i-1, dp)
    for j in range(i):
        if arr[i] % arr[j] == 0:
            ratio = arr[i]/arr[j]
            if (j, ratio) in dp:
                dp[(i, ratio)] = dp[(j, ratio)] + 1
            else:
                dp[(i, ratio)] = 2
    dp[(i,1)] = 1
    
dp = {}
arr = [1,3,7,8,9,14,25,27,67,78,81]
f(arr, len(arr)-1, dp)
print dp
