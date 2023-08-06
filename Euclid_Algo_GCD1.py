def GCD(m, n):
    if m<n:
        (m,n)=(n,m)
    
    if m%n ==0:
        return(print("The GCD is:",n))
    else:
        return(GCD(n, m-n))

m=int(input("Enter the First number:"))
n=int(input("Enter the Second number:"))

GCD(m,n)    

