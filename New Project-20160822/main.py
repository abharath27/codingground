#Rotating matrix in place..

def rotateInPlace(arr,size,startRow,startCol, n):
    if size <= 1:
        return
    
    #do the outer layer first
    for i in range(size-1):
        row = startRow + i
        #(x,y) -> (y,n-x)
        temp1 = arr[row][startCol]
        temp2 = arr[startCol][n-row-1]
        temp3 = arr[n-row-1][n-startCol-1]
        temp4 = arr[n-startCol-1][row]
        
        arr[startCol][n-row-1] = temp1
        arr[n-row-1][n-startCol-1] = temp2
        arr[n-startCol-1][row] = temp3
        arr[row][startCol] = temp4
    
    rotateInPlace(arr, size-2, startRow+1, startCol+1, n)
    
if __name__=="__main__":
    col = [None]*5
    col[0] = [1,2,3,4,20]
    col[1] = [5,6,7,8,21]
    col[2] = [9,10,11,12,22]
    col[3] = [13,14,15,16,23]
    col[4] = [17,18,19,41,42]
    rotateInPlace(col,5,0,0,5)
    print col
