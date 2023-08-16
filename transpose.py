def transpose(m):
    num_rows = len(m)
    num_cols = len(m[0])
    
    transposed = []
    for j in range(num_cols):
        transposed_row = []
        for i in range(num_rows):
            transposed_row.append(m[i][j])
        transposed.append(transposed_row)
    
    return transposed
    
transpose(m)







