def update(list,index,value):

    if(index>=0 & index<= len(list) - 1 ):
        list[index]=value
        return(print(list))
    else:
        print("Index is wrong")

list=[1,2,3,4]

update(list,2,9)