def merge_sort(list):
    if len(list)==1:
        return list
    
    mid=len(list)//2
    left=merge_sort(list[:mid])
    right=merge_sort(list[mid:])

    return merge(left,right)

def merge(left, right):
    i = 0
    j = 0
    m = len(left)
    n = len(right)
    sorted_list = []

    while i < m and j < n:
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        elif left[i] > right[j]:
            sorted_list.append(right[j])
            j += 1
        elif left[i]==right[j]:
            sorted_list.append(right[j])
            sorted_list.append(left[i])
            i += 1
            j += 1
        if i == m:
            sorted_list = sorted_list + right[j:]
        elif j == n:
            sorted_list = sorted_list + left[i:]
            

    return sorted_list

original_list=[1,34,34,34212,32453,2314,1,2]

print(merge_sort(original_list))