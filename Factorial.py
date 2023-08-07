def factorial(x):

    if x==1:
        return(x)
    
    else:
        ans=1
        while(x>0):
            ans=ans*x
            x-=1
        
    return(print(ans))

value=int(input("Enter the Number:"))
factorial(value)
