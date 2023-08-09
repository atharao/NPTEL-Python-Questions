def allfactors(x):
    factors=[]
    for i in range(1,x+1):
        if x%i ==0:
            factors.append(i)

    return(factors)

value=int(input("Enter the number:"))
print(allfactors(value))
