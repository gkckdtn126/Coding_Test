n = int(input())
score = list(map(int,input().split()))
avg = round(sum(score)/n)
gap_total = []
student_number = []
gap_not_total = []
for i in score:
    gap = abs(avg-i)
    gap_not = i-avg
    gap_total.append(gap)
    gap_not_total.append(gap_not)
student_number = [i for i, x in enumerate(gap_total) if x == min(gap_total)]
for i in student_number:
    if gap_not_total[i] < 0:
        student_number.remove(i)
if len(student_number)>1:
    print(avg,min(student_number)+1)
else:
    print(avg,student_number[0]+1)        