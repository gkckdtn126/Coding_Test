n = int(input())
check = list(map(int,input().split()))
score = [0]*n
for i in range(len(check)):
    if i == 0 and check[i] == 1:
        score[i] = 1
    elif check[i] == 1 and check[i] != check[i-1]:
        score[i] = 1
    elif check[i]== 1 and check[i] == check[i-1]:
        score[i] = score[i-1]+1
    else:
        score[i] = 0
print(sum(score))