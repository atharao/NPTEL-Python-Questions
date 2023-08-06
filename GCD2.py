CommonFactors=[]

def GCD(m,n):

    for i in range(1, min(m,n)+1):
        if m % i == 0 & n % i==0:
            CommonFactors.append(i)

    return(print("The GCD is:",max(CommonFactors)))

m=int(input("Enter the First number:"))
n=int(input("Enter the Second number:"))


GCD(m,n)    





    




