total=0
adult=0
teenager=0
kid=0
humans = int(input("몇 분이세요? "))
#ages=[None for _ in range(humans)]
ages=[]
print(ages)

for i in range(humans):
    ages.append(int(input("나이는? ")))

print(ages)

for age in ages:
    # 어른 : 20000, 청소년(8~19): 10000, 어린이:(~8): 5000
    if age>19:
        total=total+20000
        adult+=1
    elif 19 >= age >= 8:
        total=total+10000
        teenager+=1
    else:
        total=total+5000
        kid+=1
print(f"어른 {adult}명, 청소년 {teenager}명, 어린이 {kid}명 의 총 요금은 {total}원 입니다.")

