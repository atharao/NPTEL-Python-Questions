def Selection_sort(list):
    temp=0
    for i in range(len(list)):          
        for j in range(i+1,len(list)):
            if list[j]<list[i]:
                list[i],list[j]=list[j],list[i]
    return(list)
        
list=[12,3,23,24,23,23,5]            
print(Selection_sort(list))            
