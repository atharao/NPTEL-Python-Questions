def GCD(m, n):
    if m<n:
        (m,n)=(n,m)
    
    while (m%n)!=0:

        return(GCD(n, m-n))

    return(print("The GCD is:",n))
m=int(input("Enter the First number:"))
n=int(input("Enter the Second number:"))

GCD(m,n)    

