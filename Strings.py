def delchar(s,c):
    if(len(c)>1):
        return(s)
    else:
        without_s=""
        for i in s:
            if(i!=c):
                without_s +=i
        return(without_s)

value1=(input("Enter the 1st string:"))
value2=(input("Enter the 2nd string:"))
print(delchar(value1,value2))      
