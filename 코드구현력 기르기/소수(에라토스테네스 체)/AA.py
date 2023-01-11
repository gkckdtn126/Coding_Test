n = int(input())
result = 0
for i in range(2,n+1):
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count += 1
    if count == 0:
        result += 1
print(result)