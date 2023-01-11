n = int(input())
num = list(map(int,input().split()))
def reverse(x):
    sum = 0
    x = str(x)
    contain = []
    for i in x:
        contain.append(i)
    contain.reverse()
    for i in range(len(contain)):
        value = int(contain[i])*10**(len(contain)-(i+1))
        sum += value
    return sum
    
def isPrime(x):
    count = 0
    for i in range(1,x+1):
        if x%i==0:
            count += 1
    if count == 2:
        isprime = True
        return isprime
for i in num:
    number = reverse(i)
    isprime = isPrime(number)
    if isprime == True:
        print(number,end = ' ')