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

left = [10, 4, 9,12,34,5]
right = [1, 5, 6]
print(merge(left, right))
