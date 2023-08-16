def Insertion_sort(list):
    new_list=[list[0]]
    for i in range(1,len(list)):
        inserted=0
        for j in range(len(new_list)):
            if new_list[j]>list[i]:
                new_list.insert(j,list[i]) 
                inserted=1
                break
        if inserted==0:        
            new_list.append(list[i])
    return(new_list)
list=[12,3,22,24,26,20,5]            
print(Insertion_sort(list))            
