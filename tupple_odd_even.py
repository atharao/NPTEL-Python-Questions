def odd_even_split_tuple(tup):
    odd_elements = tup[0::2]  
    even_elements = tup[1::2] 
    return odd_elements, even_elements


input_tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)

odd_elements,even_elements=odd_even_split_tuple(input_tuple)

print("Odd:", odd_elements)
print("Even:", even_elements)
