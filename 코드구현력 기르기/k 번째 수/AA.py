import sys
sys.stdin=open("input.txt", "r")
t = int(input())
case_total = []
number_total = []
for _ in range(t):
    case = list(map(int,input().split()))
    case_total.append(case)
    number = list(map(int,input().split()))
    number_total.append(number)
def main(t,case_total,number_total):
    for i in range(t):
        sub_num = list(number_total[i][case_total[i][1]-1:case_total[i][2]])
        sub_num.sort()
        print("#%d"%(i+1),sub_num[case_total[i][3]-1])
main(t,case_total,number_total)