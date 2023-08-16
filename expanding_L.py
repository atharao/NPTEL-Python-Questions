def expanding(l):
    if len(l) < 3:
        return False
    
    for i in range(2, len(l)):
        if abs(l[i] - l[i - 1]) <= abs(l[i - 1] - l[i - 2]):
            return False
    return True

expanding(l)