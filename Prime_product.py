def primeproduct(m):

    fact=[]
    count=0

    if m<= 0:
        return(False)
    
    for i in range(2,m):
        if(m%i== 0):
            fact.append(i)

    for j in fact:
        for k in range(2,j):
            if(j%k==0):
                break
        count +=1
            
    if count==2:
        return(True)
    else:
        return(False)

value=int(input("Enter the number:"))   
print(primeproduct(value))     

        

