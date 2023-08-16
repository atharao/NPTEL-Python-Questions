def binary_search(list,l,r,value):
    list.sort() 
    if r>=l:
        mid=int((l+r)/2)
    
        if list[mid] ==value:
            return(True)
        elif list[mid]> value:
            return(binary_search(list,l,mid-1,value))
        
        elif list[mid]< value:
            return(binary_search(list,mid+1,r,value))
    else:
        return(False)



list=[1,2,34,355,4532,23524,235235,32]
value=355
l=0
r=(len(list)-1)
print(binary_search(list,l,r,value))

        




