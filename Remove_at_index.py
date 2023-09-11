def remove():   
    list1=[]
    N=int(input("Number of Elements:"))
    for i in range(N):
        A=int(input("Enter the "+ str(i) +" number:"))
        list1.append(A)

    X=int(input("Index of Number to be removed:"))
    del list1[X]
    for i in list1:
        print(i,end=" ")
(remove())