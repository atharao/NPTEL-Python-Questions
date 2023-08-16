def sumsquare(l):
    odd_sum = sum(x ** 2 for x in l if x % 2 != 0)
    even_sum = sum(x ** 2 for x in l if x % 2 == 0)
    return [odd_sum, even_sum]


sumsquare(l)      
