def histogram(l):
    
    count_dict = {}
    for num in l:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    
    pairs = [(num, count) for num, count in count_dict.items()]
    sorted_pairs = sorted(pairs, key=lambda x: (x[1], x[0]))
    
    return sorted_pairs
    
print(histogram([13,12,11,13,14,13,7,7,13,14,12]))