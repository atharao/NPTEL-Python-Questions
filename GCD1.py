Factor_m,Factor_n,CommonFactors=[],[],[]

def GCD(m,n):

    for i in range(1,m+1):
        if m % i == 0:
           Factor_m.append(i) 

    for j in range(1,n+1):
        if n % j == 0:
           Factor_n.append(j)  

    for k in Factor_m:
        for l in Factor_n:
            if k==l:
                CommonFactors.append(k)

    return(print("The GCD is:",max(CommonFactors)))

m=int(input("Enter the First number:"))
n=int(input("Enter the Second number:"))

   
GCD(m,n)    





    




