import sys
#sys.stdin=open("input.txt", "r")
n,k = map(int,input().split())
card = list(map(int,input().split()))
case = []
for i in range(n):
    for j in range(i,n):
        if i != j:
            for w in range(j,n):
                if j !=w:
                    sub = [card[i],card[j],card[w]]
                    case.append(sum(sub))

case = set(case)
case = list(case)
case.sort()
print(case[k*-1])