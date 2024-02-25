def isEven(n):
    if(n%2==0):
        return True
    else:
        return False

def even(start, end):
    arr=[]
    for i in range(start , end+1):
        if(isEven(i)):
            arr.append(i)
    return arr
    