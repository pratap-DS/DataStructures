# Enter your code here. Read input from STDIN. Print output to STDOUT
def validArray(ar,m,k):
    iterations = 0

    i = 0
    n = len(ar)
    summ = 0
    cnt = 0
    while(i<n):
        summ += ar[i]
        if summ <= m:
            # print("--",m,summ,ar[i])
            i += 1
        else:
            # print("--XX",m,summ,ar[i],count)
            summ = ar[i]
            cnt += 1
            i += 1

    if summ < m:
        cnt += 1

    return cnt <= k


t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    ar = list(map(int,input().split()))

    n,k = 10, 3
    ar = [1,10,13,4,5,12,23,12,18,8]

    l = max(ar)
    h = sum(ar)
    ans = -1
    while(l<h):
        # print(l,h)
        m = (l+h)//2
        if validArray(ar, m, k):
            h = m-1
            ans = m
            # print(ans)
        else:
            l = m+1
    
    print(ans)

    