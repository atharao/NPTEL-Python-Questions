all_primes = []

def totalprimes(x):
    if x == 0 or x == 1:
        return print("there is no prime number")
    else:
        for i in range(2, x + 1):
            flag = 0
            for j in range(2, i):
                if i % j == 0:
                    break
        
            flag = 1

            if flag == 1:
                all_primes.append(i)
value=int(input("Enter the number:"))
totalprimes(value)
print(all_primes)
