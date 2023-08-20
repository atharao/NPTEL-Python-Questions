def sumsquare(l):
    sum_odd=0
    sum_even=0

    for i in l:
        if i%2!=0:
            sum_odd=sum_odd+i*i
        else:
            sum_even=sum_even+i*i   

    return([sum_odd,sum_even])
l=[-1,-2,3,7]

print(sumsquare(l))