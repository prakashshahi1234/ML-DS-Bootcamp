def takeValue():
    print("taking matrix values")
    m = int(input("enter row of matrix"))
    n = int(input("enter column of matrix"))
    mat= []
    for i in range(0,m):
        row = []
        for j in range(0,n):
            row.append( int(input("enter value")))
        mat.append(row)
    return mat


def multiPly(mat):
    row = len(mat)
    col = len(mat[0])
    result = []
    for i in range(row):
        row_re = []
        for j in range(col):      
            dotProduct=0
            for k in range(row):
                dotProduct = mat[i][k]*mat[k][i]
            row_re.append(dotProduct)
        result.append(row_re)
    return result
            
                
                
    
                       