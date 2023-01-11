n = int(input())
a = []
for i in range(n):
    a.append(str(input()).lower()) #대문자는 문자.upper()
for index,i in enumerate(a):
    b = list(i)
    c = b.copy()
    b.reverse()
    if c == b:
        print("#%d YES"%(index+1))
    else:
        print("#%d NO"%(index+1))