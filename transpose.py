def transpose(m):
    transposed = []
    for j in range(len(m[0])):
        transposed_row = []
        for i in range(len(m)):
            transposed_row.append(m[i][j])
        transposed.append(transposed_row)
    
    return transposed
m=[[2]]  
print(transpose(m))







