n,m = map(int,input().split())
list_n = list(range(1,n+1))
list_m = list(range(1,m+1))
sum_total = []
for i in list_n:
    for j in list_m:
        sum_total.append(i+j)
count_total = []
for index,value in enumerate(sum_total):
    count_total.append(sum_total.count(value))
index_total = []
for index,value in enumerate(sum_total):
    if sum_total.count(value) == max(count_total):
        index_total.append(index)
num = []
for i in index_total:
    num.append(sum_total[i])
num = set(num)
num = list(num)
num.sort()
for i in num:
    print(i, end=' ')