def expanding(l):
    if len(list) < 3 :
        return False
    diff=list[1]-list[0]
    for i in range (2,len(list)):
        if abs(list[i]-list[i-1])> diff:
            diff=abs(list[i]-list[i-1])
        else:
            return False
    return True


list=[2,2,2,2222,22222]
print(expanding(list))