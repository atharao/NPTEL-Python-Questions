
def isprime(x):
    if (x==0 & x==1):
        return(False)

    else:
        for i in range(2,x):
            if (x%i==0):
                return(False)
    
        return(True)


isprime(7)
    