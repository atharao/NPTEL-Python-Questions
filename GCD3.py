def GCD(m,n):

    i=(min(m,n))
    while(i>0):
        if m % i == 0 & n % i==0:
            return(print(i))
        else:
             i-=1


m=int(input("Enter the First number:"))
n=int(input("Enter the Second number:"))

   
GCD(m,n)    





    




