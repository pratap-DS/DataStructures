def isPrime(t):
    k = int(t ** 0.5)+1
    ans = True
    for i in range(2,k):

        if t%i == 0:
            ans = False
            break

    if ans and t>1:
        return True
    else:
        return False



def leadingRemoval(n):
    length = len(str(n))

    a = n 
    b = 10**(length-1)
    ans = True
    while(b>1):
        a = a%b
        print(a)
        if not isPrime(a):
            ans = False
            break
        b = b //10

    return ans


crt = leadingRemoval(3797)
print(crt)


