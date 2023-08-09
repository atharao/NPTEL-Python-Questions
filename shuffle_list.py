def shuffle(l1,l2):
    l3=[]
    minimum=min((len(l1),len(l2)))    
    for i in range(minimum):
        l3.append(l1[i])
        l3.append(l2[i])

    if len(l1)>minimum:
        l3=l3+l1[minimum:]

    if len(l2)>minimum:
        l3=l3+l2[minimum:]

    return(l3)

n = int (input ("Enter number of elements in First list: ")) 
l1 = []

for i in range (n):
    x = int(input("Enter the Elements of First list:"))
    l1.append(x)

m = int (input ("Enter number of elements in Second list: ")) 
l2 = []

for i in range (m):
    x = int(input("Enter the Elements of Second list:"))
    l2.append(x)



print(shuffle(l1,l2))



