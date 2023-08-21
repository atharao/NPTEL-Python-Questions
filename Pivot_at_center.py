def pivot_center(list):
    for i in range (len(list)):
        pivot=list[0]
        p=1
        q=len(list)-1

        while (p<len(list)):
            if list[p]>=pivot:
                break
            p=p+1
        while (q>=0):
            if list[q]<=pivot:
                break
            q=q-1
        if q>p:
            list[p],list[q]=list[q],list[p]

        else:
            list[q],list[0]=list[0],list[q]
            break
        
    return list
    
Un_sorted=[35,50,15,25,80,20,90,45]
print(pivot_center(Un_sorted))