b = list(range(1,21))
for i in range(1,11):
    n,m = map(int,input().split())
    c = b[n-1:m]
    c.reverse()
    b[n-1:m] = c
for i in b:
    print(i, end = ' ')