def isOdd(n):
    if(n%2!=0):
        return True
    else:
        return False

def odd(start, end):
    arr=[]
    for i in range(start , end+1):
        if(isOdd(i)):
            arr.append(i)
    return arr
    