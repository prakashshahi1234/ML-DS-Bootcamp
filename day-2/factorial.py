def fact(n):
    if n<0:
        return "impossible"
    if(n==1):
        return 1
    x=1
    for i in range(n ,0 , -1):
        x=x*i
    return x
           
        