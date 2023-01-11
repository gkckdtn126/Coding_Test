n = int(input())
x = list(map(int,input().split()))
def digit_sum(x):
    
    sum_total_compare = 0
    result = []
    count = 0
    for i in x:
        i = str(i)
        sum_total = []
        for j in i:
            sum_total.append(int(j))
        result.append(sum(sum_total))
    answer = max(result)
    print(x[result.index(answer)])
digit_sum(x)  