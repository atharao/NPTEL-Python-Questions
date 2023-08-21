def Quick_sort(list,start,end):
    pivot_pos=start
    if  start < end:    
        pivot=list[start]
        p=start+1
        q=end-1

        while p<=q:

            while (p<end):
                if list[p]>=pivot:
                    break
                p=p+1
            while (q>=start):
                if list[q]<=pivot:
                    break
                q=q-1
            if q>p:
                list[p],list[q]=list[q],list[p]

            else:
                list[q],list[start]=list[start],list[q]
                pivot_pos=q
                break

                
        Quick_sort(list,start,pivot_pos)
        Quick_sort(list,pivot_pos+1,end)

    return list

Un_sorted=[35,50,15,25,80,20,90,45]
print(Quick_sort(Un_sorted,0,len(Un_sorted)))