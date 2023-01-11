n = int(input())
number_total = []
price_total = []
for i in range(n):
    number_total.append(list(map(int,input().split())))
for i in range(n):
    a = number_total[i]
    b = set(a)
    c = list(b)
    if len(a)-len(c) == 2:
        for i in range(len(c)):
            if c[i] in a:
                a.remove(c[i])
        price = 10000+a[0]*1000
        price_total.append(price)
    elif len(a)-len(c) == 1:
        for i in range(len(c)):
            if c[i] in a:
                a.remove(c[i])
        price = 1000+a[0]*100
        price_total.append(price)
    else:
        price = max(a)*100
        price_total.append(price)
print(max(price_total))